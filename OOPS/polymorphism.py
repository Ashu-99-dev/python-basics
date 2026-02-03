# polymorphism
# it is a Greek word which means many forms
# it is a ability of an object to take many forms

# class Dog:
#     def speak(self):
#         print("Woof!")

# class Cat:
#     def speak(self):
#         print("Meow!")

# class Duck:
#     def speak(self):
#         print("Quack!")

# animals = [Dog(), Cat(), Duck()]

# for animal in animals:
#     animal.speak()

# print(1 + 3)
# print("1" + "3")
# print([1,2,3] + [4,5,6])
# print("Ashutosh" + " Tiwari")

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self, num):
        real = self.real + num.real
        img = self.img + num.img
        return Complex(real, img)

    def __sub__(self, num):
        real = self.real - num.real
        img = self.img - num.img
        return Complex(real, img)
    

num1 = Complex(1, 2)
num2 = Complex(3, 4)

num3 = num1 + num2
num4 = num1 - num2
num3.showNumber()
num4.showNumber()


