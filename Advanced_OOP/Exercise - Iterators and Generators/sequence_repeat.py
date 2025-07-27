class sequence_repeat:
    def __init__(self, iterable, num):
        self.iterable = iterable
        self.num = num
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.num:
            i = self.i % len(self.iterable)
            self.i += 1
            return self.iterable[i]
        raise StopIteration


