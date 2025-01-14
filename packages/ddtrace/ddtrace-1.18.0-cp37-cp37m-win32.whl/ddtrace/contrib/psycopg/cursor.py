from ddtrace.contrib import dbapi


class Psycopg3TracedCursor(dbapi.TracedCursor):
    """TracedCursor for psycopg instances"""

    def __init__(self, cursor, pin, cfg, *args, **kwargs):
        super(Psycopg3TracedCursor, self).__init__(cursor, pin, cfg)

    def _trace_method(self, method, name, resource, extra_tags, dbm_propagator, *args, **kwargs):
        # treat Composable resource objects as strings
        if resource.__class__.__name__ == "SQL" or resource.__class__.__name__ == "Composed":
            resource = resource.as_string(self.__wrapped__)
        return super(Psycopg3TracedCursor, self)._trace_method(
            method, name, resource, extra_tags, dbm_propagator, *args, **kwargs
        )


class Psycopg3FetchTracedCursor(Psycopg3TracedCursor, dbapi.FetchTracedCursor):
    """Psycopg3FetchTracedCursor for psycopg"""


class Psycopg2TracedCursor(Psycopg3TracedCursor):
    """TracedCursor for psycopg2"""


class Psycopg2FetchTracedCursor(Psycopg3FetchTracedCursor):
    """FetchTracedCursor for psycopg2"""
