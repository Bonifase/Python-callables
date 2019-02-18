def my_decorator(f):
    def wrap(*args, **kwargs):
        escaped = f(*args, **kwargs)
        return ascii(escaped)
    return wrap


@my_decorator
def my_function():
    return "My name"
