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

class Cat:
    def sound(self):
        return "Miyov"

class Dog:
    def sound(self):
        return "Vov"

def make_sound(animal):
    print(animal.sound())

make_sound(Cat())
make_sound(Dog())
