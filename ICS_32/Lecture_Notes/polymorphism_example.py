from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, name) -> None:
        self.name = name
        
    @abstractmethod
    def area(self):
        print("Calculating area for: " + self.name)

class Rectangle(Shape):
    def __init__(self, name, r_len, r_width) -> None:
        super().__init__(name)
        self.r_len = r_len
        self.r_width = r_width
    def area(self):
        return self.r_width * self.r_len
    def prem(self):
        return (2 * self.r_width) + (2 * self.r_len)

class Rectangular_Cube (Rectangle):
    def __init__(self, name, r_len, r_width) -> None:
        super().__init__(name, r_len, r_width)

    def surface_area(self):
        pass
class Circle(Shape):
    def __init__(self, name, radius) -> None:
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

def enlarge(my_shape):
    my_shape.prem()
    print("You want to enlarge: ")
if __name__ == "__main__":
    s = Shape("Some Shape")
    r = Rectangle("Rectangle", 10, 20)
    c = Circle("Circle", 5)

    #s.area() remove this bc it is abstract
    print(r.area())
    print(c.area())

    #enlarge(s) remove because you can't have s bc abstracted
    enlarge(r)
    enlarge(c)