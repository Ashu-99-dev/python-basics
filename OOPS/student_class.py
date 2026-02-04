class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    @staticmethod # it doesn't take self as a parameter because it doesn't use any instance variable
    def welcome():
        print("Welcome to MIT")
    def avg(self):
        print(f"{self.name} your average score is: {sum(self.marks) / len(self.marks)}")


s1 = Student("Karan", [90, 80, 70])
s2 = Student("Ashutosh", [95, 85, 75])

s1.avg()
s2.avg()

s1.welcome()
s1.name = "Amit kumar"
s1.avg()






