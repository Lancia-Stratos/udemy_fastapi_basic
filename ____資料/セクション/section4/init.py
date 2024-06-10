class Person:
    height = 10
    def __init__(self, name, age): # コンストラクタ(イニシャライザ)
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"名前は{self.name}。年齢は{self.age}です。")

person1 = Person("三苫", 25)
person2 = Person("道安", 28)
person1.greet()
person2.greet()
print(person1.height)
print(person2.height)