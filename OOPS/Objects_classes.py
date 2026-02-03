# class creation
class Student:
    #default constructor it will create automatically if we don't create any constructor
    # def __init__(self):
    #     print("Adding new name in database")
    #parameterized constructor

    college_name = "MIT" # class attribute it will store in memory only once
    name = "anonymous"
    def __init__(self, name , marks):
        self.name = name
        # obj attribute it will store in memory for each object
        # its precedence is higher than class attribute
        self.marks = marks
    # instance method it will take self as a parameter    
    def welcome(self):
        print("Welcome to MIT" , self.name)
    
    def get_marks(self):
        return self.marks




# object creation
s1 = Student("Karan Kumar", 90)
print(s1.name, s1.marks , s1.college_name)
s1.welcome()
print(s1.get_marks())





