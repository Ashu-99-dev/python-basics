class Student:
    def __init__(self,phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property # it is a decorator which is used to make a method as a property and it will automatically call when we access the method
    def percentage(self):
        return (self.phy + self.chem + self.math) / 3

s1 = Student(90, 80, 70)
print(s1.percentage)

s1.phy = 100
print(s1.percentage)