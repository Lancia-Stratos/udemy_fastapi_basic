from typing import List

def add_numbers(a: int ,b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"hello, {name}"

def list_sum(numbers: List[int]) -> int:
    return sum(numbers)

print(add_numbers(5, 3))
print(greet("tanaka"))
print(list_sum([1, 2, 3]))