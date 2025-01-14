import ctypes
import struct

# 3p
import bson
from bson.codec_options import CodecOptions
from bson.son import SON

# project
from ...ext import net as netx
from ...internal.compat import to_unicode
from ...internal.logger import get_logger


log = get_logger(__name__)


# MongoDB wire protocol commands
# http://docs.mongodb.com/manual/reference/mongodb-wire-protocol
OP_CODES = {
    1: "reply",
    1000: "msg",  # DEV: 1000 was deprecated at some point, use 2013 instead
    2001: "update",
    2002: "insert",
    2003: "reserved",
    2004: "query",
    2005: "get_more",
    2006: "delete",
    2007: "kill_cursors",
    2010: "command",
    2011: "command_reply",
    2013: "msg",
}

# The maximum message length we'll try to parse
MAX_MSG_PARSE_LEN = 1024 * 1024

header_struct = struct.Struct("<iiii")


class Command(object):
    """Command stores information about a pymongo network command,"""

    __slots__ = ["name", "coll", "db", "tags", "metrics", "query"]

    def __init__(self, name, db, coll):
        self.name = name
        self.coll = coll
        self.db = db
        self.tags = {}
        self.metrics = {}
        self.query = None

    def __repr__(self):
        return ("Command(" "name=%s," "db=%s," "coll=%s)") % (self.name, self.db, self.coll)


def parse_msg(msg_bytes):
    """Return a command from a binary mongo db message or None if we shouldn't
    trace it. The protocol is documented here:
    http://docs.mongodb.com/manual/reference/mongodb-wire-protocol
    """
    # NOTE[matt] this is used for queries in pymongo <= 3.0.0 and for inserts
    # in up to date versions.
    msg_len = len(msg_bytes)
    if msg_len <= 0:
        return None

    header = header_struct.unpack_from(msg_bytes, 0)
    (length, req_id, response_to, op_code) = header

    op = OP_CODES.get(op_code)
    if not op:
        log.debug("unknown op code: %s", op_code)
        return None

    db = None
    coll = None

    offset = header_struct.size
    cmd = None
    if op == "query":
        # NOTE[matt] inserts, updates and queries can all use this opcode

        offset += 4  # skip flags
        ns = _cstring(msg_bytes[offset:])
        offset += len(ns) + 1  # include null terminator

        # note: here coll could be '$cmd' because it can be overridden in the
        # query itself (like {'insert':'songs'})
        db, coll = _split_namespace(ns)

        offset += 8  # skip numberToSkip & numberToReturn
        if msg_len <= MAX_MSG_PARSE_LEN:
            # FIXME[matt] don't try to parse large messages for performance
            # reasons. ideally we'd just peek at the first bytes to get
            # the critical info (op type, collection, query, # of docs)
            # rather than parse the whole thing. i suspect only massive
            # inserts will be affected.
            codec = CodecOptions(SON)
            spec = next(bson.decode_iter(msg_bytes[offset:], codec_options=codec))
            cmd = parse_spec(spec, db)
        else:
            # let's still note that a command happened.
            cmd = Command("command", db, "untraced_message_too_large")

        # If the command didn't contain namespace info, set it here.
        if not cmd.coll:
            cmd.coll = coll
    elif op == "msg":
        # Skip header and flag bits
        offset += 4

        # Parse the msg kind
        kind = ord(msg_bytes[offset : offset + 1])
        offset += 1

        # Kinds: https://docs.mongodb.com/manual/reference/mongodb-wire-protocol/#sections
        #   - 0: BSON Object
        #   - 1: Document Sequence
        if kind == 0:
            if msg_len <= MAX_MSG_PARSE_LEN:
                codec = CodecOptions(SON)
                spec = next(bson.decode_iter(msg_bytes[offset:], codec_options=codec))
                cmd = parse_spec(spec, db)
            else:
                # let's still note that a command happened.
                cmd = Command("command", db, "untraced_message_too_large")
        else:
            # let's still note that a command happened.
            cmd = Command("command", db, "unsupported_msg_kind")

    if cmd:
        cmd.metrics[netx.BYTES_OUT] = msg_len
    return cmd


def parse_query(query):
    """Return a command parsed from the given mongo db query."""
    db, coll = None, None
    ns = getattr(query, "ns", None)
    if ns:
        # version < 3.1 stores the full namespace
        db, coll = _split_namespace(ns)
    else:
        # version >= 3.1 stores the db and coll separately
        coll = getattr(query, "coll", None)
        db = getattr(query, "db", None)

    # pymongo < 3.1 _Query does not have a name field, so default to 'query'
    cmd = Command(getattr(query, "name", "query"), db, coll)
    cmd.query = query.spec
    return cmd


def parse_spec(spec, db=None):
    """Return a Command that has parsed the relevant detail for the given
    pymongo SON spec.
    """

    # the first element is the command and collection
    items = list(spec.items())
    if not items:
        return None
    name, coll = items[0]
    cmd = Command(name, db or spec.get("$db"), coll)

    if "ordered" in spec:  # in insert and update
        cmd.tags["mongodb.ordered"] = spec["ordered"]

    if cmd.name == "insert":
        if "documents" in spec:
            cmd.metrics["mongodb.documents"] = len(spec["documents"])

    elif cmd.name == "update":
        updates = spec.get("updates")
        if updates:
            # FIXME[matt] is there ever more than one here?
            cmd.query = updates[0].get("q")

    elif cmd.name == "delete":
        dels = spec.get("deletes")
        if dels:
            # FIXME[matt] is there ever more than one here?
            cmd.query = dels[0].get("q")

    return cmd


def _cstring(raw):
    """Return the first null terminated cstring from the buffer."""
    return ctypes.create_string_buffer(raw).value


def _split_namespace(ns):
    """Return a tuple of (db, collection) from the 'db.coll' string."""
    if ns:
        # NOTE[matt] ns is unicode or bytes depending on the client version
        # so force cast to unicode
        split = to_unicode(ns).split(".", 1)
        if len(split) == 1:
            raise Exception("namespace doesn't contain period: %s" % ns)
        return split
    return (None, None)
