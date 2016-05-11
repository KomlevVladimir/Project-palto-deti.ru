class Sizes(object):

    def __init__(self, size=None):
        self.size = size

    @classmethod
    def Size104(cls):
        return cls(size="11")

    @classmethod
    def Size110(cls):
        return cls(size="116")

    @classmethod
    def Size116(cls):
        return cls(size="122")

    @classmethod
    def Size122(cls):
        return cls(size="128")

    @classmethod
    def Size134(cls):
        return cls(size="134")

    @classmethod
    def Size128(cls):
        return cls(size="140")

    @classmethod
    def Size140(cls):
        return cls(size="104")