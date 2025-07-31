class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.current = len(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        self.current -= 1
        if self.current < 0:
            raise StopIteration
        return self.iterable[self.current]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
