# Define a Employee class with attributes role, department & salary. This class has a method showDetails
# Create an Engineer class that inherits proprtties from Employee& 

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print(f"Role: {self.role}\nDepartment: {self.department}\nSalary: {self.salary}")


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75000")

    def showDetails(self):
        print(f"Name: {self.name}\nAge: {self.age}\nRole: {self.role}\nDepartment: {self.department}\nSalary: {self.salary}")


eng1 = Engineer("Ashutosh", 24)  # String must be in quotes!
eng1.showDetails()
