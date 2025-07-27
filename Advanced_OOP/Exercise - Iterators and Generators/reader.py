def read_next(*args):
    for iterable in args:
        for item in iterable:
            yield item
