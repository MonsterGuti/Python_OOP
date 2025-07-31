def tags(param):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = f"<{param}>{func(*args, **kwargs)}</{param}>"
            return result
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
