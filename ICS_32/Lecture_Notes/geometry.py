#Important note about "self": Self is the pointer to the object that methos use to access the object
class Rectangle:
    number_of_rectangles = 0 #This isn't a instance var. This is a class var and belongs to the class
    #Constructor is being ignored because Python looks at the last constructor defined in the fiel
    def __init__(self,):
        self.length = 0
        self.width = 0
        self.color = ""
    def __init__(self, length: int, width: int, color: str):
        self.length = length
        self.width = width
        self.color = color
    #Str method is part of the python language, and it is used to print the content of an object
        #The string is "Private method!" What this means is it shouldn't be called from outside the class
        #Python doesn't support private access, so this is just a convention the convention for private is __functionName__
    def __str__(self):
        my_string = "Length: " + str(self.length) + ", width: " + str(self.width) + ", color: " + self.color

if __name__ == "__main__":
    print("rpractice w classes and objects")

    r1 = Rectangle(10, 5, "Red")

    r2 = Rectangle(5, 2, "Green")

    print(r1.length)
    print(r2.length)