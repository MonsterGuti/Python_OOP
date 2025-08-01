def logged(function):
    def wrapper(*args):
        result = function(*args)
        return f"you called {function.__name__}{args}\nit returned {result}"
    return wrapper



@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))
