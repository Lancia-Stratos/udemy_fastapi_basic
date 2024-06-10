def simple_decorator(func):
    def wrapper():
        print("デコレータ内の関数")
        func()
    return wrapper

@simple_decorator
def say_hello():
    print("hello")

say_hello()