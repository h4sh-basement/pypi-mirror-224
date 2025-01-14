class Input_info(object):
    __slots__ = ["name", "value", "origin"]

    def __init__(self, name, value, origin):
        self.name = name
        self.value = value
        self.origin = origin

    def __eq__(self, other):
        return self.name == other.name and self.value == other.value and self.origin == other.origin

    def __repr__(self):
        return "input_info(%s, %s, %s)" % (str(self.name), str(self.value), str(self.origin))
