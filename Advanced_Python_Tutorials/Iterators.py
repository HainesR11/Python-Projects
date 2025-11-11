class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        """Return the next value from the range."""
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
