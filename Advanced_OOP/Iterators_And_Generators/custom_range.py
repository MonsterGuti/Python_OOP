class custom_ange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.current = start - 1


    def __iter__(self):
        return self


    def __next__(self):
        self.current += 1
        if self.current > self.stop:
            raise StopIteration
        return self.current


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
