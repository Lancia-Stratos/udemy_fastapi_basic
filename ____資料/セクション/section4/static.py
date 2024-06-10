class MathClass:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiple(a, b):
        return a * b

# math = MathClass() # インスタンス化
result_add = MathClass.add(5, 3)
result_multiple = MathClass.multiple(5, 3)
print(result_add, result_multiple)
