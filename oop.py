# class Car:
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year

#     def info(self):
#         return f"{self.year} yildagi {self.model}"

# car1 = Car("Lacetti", 2020)
# print(car1.info())

# meros olish
# class Animal:
#     def speak(self):
#         return "Nimadir tovush chiqaryapti"

# class Dog(Animal):
#     def speak(self):
#         return "Vov-vov!"

# dog = Dog()
# print(dog.speak())


# class Account:
#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance

# acc = Account(1000)
# acc.deposit(500)
# print(acc.get_balance())

# class Cat:
#     def sound(self):
#         return "Miyov"

# class Dog:
#     def sound(self):
#         return "Vov"

# def make_sound(animal):
#     print(animal.sound())

# make_sound(Cat())
# make_sound(Dog())

# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     def info(self):
#         return f"{self.name} - {self.grade}-sinfi"

# s1 = Student("Ali", 9)
# print(s1.info())


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# r = Rectangle(4, 5)
# print("Yuza:", r.area())

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             return f"{amount} yechildi. Qolgan: {self.balance}"
#         return "Yetarli mablag' yo'q"

# b = BankAccount("Javlon", 2000)
# print(b.withdraw(500))

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show(self):
        return f"{self.title} by {self.author}"

books = [
    Book("Alkimyogar", "Paulo Coelho"),
    Book("Kichkina shahzoda", "Exupery")
]

for b in books:
    print(b.show())
