class Student:
    name = "Anonymous"
    def __init__(self,name):
        self.name = name


##### A class method is bound to the class & recevices the class as an implicit first argument

## Note - static method doesn't access or modify the class state & generally for uitility

    @classmethod
    def change_name(cls, name):
        cls.name = name

s1 = Student("Rahul kumar")
print(s1.name)

Student.change_name("Ashutosh")

print(Student.name)