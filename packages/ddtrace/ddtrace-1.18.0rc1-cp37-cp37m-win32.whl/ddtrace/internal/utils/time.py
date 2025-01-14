from datetime import datetime
from datetime import timedelta
from types import TracebackType
from typing import Optional
from typing import Type

from ddtrace.internal import compat
from ddtrace.internal.logger import get_logger


log = get_logger(__name__)


def fromisoformat_py2(t):
    # type: (str) -> datetime
    """Alternative function to datetime.fromisoformat that does not exist in python 2. This function parses dates with
    this format: 2022-09-01T01:00:00+02:00
    """
    ret = datetime.strptime(t[:19], "%Y-%m-%dT%H:%M:%S")
    if t[19] == "+":
        ret -= timedelta(hours=int(t[20:22]), minutes=int(t[23:]))
    elif t[19] == "-":
        ret += timedelta(hours=int(t[20:22]), minutes=int(t[23:]))
    return ret


def parse_isoformat(date):
    # type: (str) -> Optional[datetime]
    if date.endswith("Z"):
        try:
            return datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            return datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    try:
        if hasattr(datetime, "fromisoformat"):
            return datetime.fromisoformat(date)
        else:
            return fromisoformat_py2(date)
    except (ValueError, IndexError):
        log.debug("unsupported isoformat: %s", date)
    return None


class StopWatch(object):
    """A simple timer/stopwatch helper class.

    Not thread-safe (when a single watch is mutated by multiple threads at
    the same time). Thread-safe when used by a single thread (not shared) or
    when operations are performed in a thread-safe manner on these objects by
    wrapping those operations with locks.

    It will use the `monotonic`_ pypi library to find an appropriate
    monotonically increasing time providing function (which typically varies
    depending on operating system and Python version).

    .. _monotonic: https://pypi.python.org/pypi/monotonic/
    """

    def __init__(self):
        # type: () -> None
        self._started_at = None  # type: Optional[float]
        self._stopped_at = None  # type: Optional[float]

    def start(self):
        # type: () -> StopWatch
        """Starts the watch."""
        self._started_at = compat.monotonic()
        return self

    def elapsed(self):
        # type: () -> float
        """Get how many seconds have elapsed.

        :return: Number of seconds elapsed
        :rtype: float
        """
        # NOTE: datetime.timedelta does not support nanoseconds, so keep a float here
        if self._started_at is None:
            raise RuntimeError("Can not get the elapsed time of a stopwatch" " if it has not been started/stopped")
        if self._stopped_at is None:
            now = compat.monotonic()
        else:
            now = self._stopped_at
        return now - self._started_at

    def __enter__(self):
        # type: () -> StopWatch
        """Starts the watch."""
        self.start()
        return self

    def __exit__(self, tp, value, traceback):
        # type: (Optional[Type[BaseException]], Optional[BaseException], Optional[TracebackType]) -> None
        """Stops the watch."""
        self.stop()

    def stop(self):
        # type: () -> StopWatch
        """Stops the watch."""
        if self._started_at is None:
            raise RuntimeError("Can not stop a stopwatch that has not been" " started")
        self._stopped_at = compat.monotonic()
        return self


class HourGlass(object):
    """An implementation of an hourglass."""

    def __init__(self, duration):
        # type: (float) -> None
        t = compat.monotonic()

        self._duration = duration
        self._started_at = t - duration
        self._end_at = t

        self.trickling = self._trickled  # type: ignore[assignment]

    def turn(self):
        # type: () -> None
        """Turn the hourglass."""
        t = compat.monotonic()
        top_0 = self._end_at - self._started_at
        bottom = self._duration - top_0 + min(t - self._started_at, top_0)

        self._started_at = t
        self._end_at = t + bottom

        self.trickling = self._trickling  # type: ignore[assignment]

    def trickling(self):
        # type: () -> bool
        """Check if sand is still trickling."""
        return False

    def _trickled(self):
        # type: () -> bool
        return False

    def _trickling(self):
        # type: () -> bool
        if compat.monotonic() < self._end_at:
            return True

        # No longer trickling, so we change state
        self.trickling = self._trickled  # type: ignore[assignment]

        return False

    def __enter__(self):
        # type: () -> HourGlass
        self.turn()
        return self

    def __exit__(self, tp, value, traceback):
        pass
