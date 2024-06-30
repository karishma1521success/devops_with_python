# decorators - just like toll in road, all veichles has to pass from toll only
# same all function has to pass from decorators while executing


def decorator_fun(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling:  {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args,**kwargs)
    return wrapper


@decorator_fun
def greet(name, greeting = "hello"):
    print(f"{greeting} {name}")


greet("chai", greeting="hanji")


