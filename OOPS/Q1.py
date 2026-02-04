# Define a Circle class to create a circle with radius r using the constructor.
# Definr area Area() method of the class which claculates the area of the circle.
# Define circumference() method of the class which calculates the circumference of the circle.


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def Area(self):
        print(f"Area of the circle whose radius {self.radius} is: {(22/7)*self.radius**2}")

    def circumference(self):
        print(f"Circumfarence of circle whose radius {self.radius} is: {2*(22/7)*self.radius}")


c1 = Circle(7)
c1.Area()
c1.circumference()