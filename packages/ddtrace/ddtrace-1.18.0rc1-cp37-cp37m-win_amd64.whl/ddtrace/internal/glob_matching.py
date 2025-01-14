from .utils.cache import cachedmethod


class GlobMatcher(object):
    """This is a backtracking implementation of the glob matching algorithm.
    The glob pattern language supports `*` as a multiple character wildcard which includes matches on `""`
    and `?` as a single character wildcard, but no escape sequences.
    The match method will be cached for quicker matching and is in a class to keep it from being global.
    """

    def __init__(self, pattern):
        # type: (str) -> None
        self.pattern = pattern

    @cachedmethod()
    def match(self, subject):
        # type: (str) -> bool
        pattern = self.pattern
        px = 0  # [p]attern inde[x]
        sx = 0  # [s]ubject inde[x]
        nextPx = 0
        nextSx = 0

        while px < len(pattern) or sx < len(subject):
            if px < len(pattern):
                char = pattern[px]

                if char == "?":  # single character wildcard
                    if sx < len(subject):
                        px += 1
                        sx += 1
                        continue

                elif char == "*":  # zero-or-more-character wildcard
                    nextPx = px
                    nextSx = sx + 1
                    px += 1
                    continue

                elif sx < len(subject) and subject[sx] == char:  # default normal character match
                    px += 1
                    sx += 1
                    continue

            if 0 < nextSx <= len(subject):
                px = nextPx
                sx = nextSx
                continue

            return False
        return True
