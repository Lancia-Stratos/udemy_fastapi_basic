def print_args(*args): # タプル
    for arg in args:
        print(arg)

print_args("apple", "banana", "cherry", "melon")

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"key: {key}, value: {value}")

print_kwargs(apple="green", banana="yellow", cherry="red")