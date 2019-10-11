def my_decorator(f):
    def wrap(*args, **kwargs):
        escaped = f(*args, **kwargs)
        return ascii(escaped)
    return wrap


@my_decorator
def my_function():
    return "My name"


class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __init__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    print('Hello {}'.format(name))
