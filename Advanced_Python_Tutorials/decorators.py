def custom_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function.")
        result = func(*args, **kwargs)
        print("After calling the function.")
        return result

    return wrapper


# will be called inside the decorator wrapper function
@custom_decorator
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Alice")