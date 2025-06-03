# class Car:
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year

#     def info(self):
#         return f"{self.year} yildagi {self.model}"

# car1 = Car("Lacetti", 2020)
# print(car1.info())

# meros olish
class Animal:
    def speak(self):
        return "Nimadir tovush chiqaryapti"

class Dog(Animal):
    def speak(self):
        return "Vov-vov!"

dog = Dog()
print(dog.speak())
