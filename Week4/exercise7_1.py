# The Rectangle class
# Author: Brian Hamburg

import math

class Rectangle:
    # Construct a rectangle object
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

    def getArea(self):
        return self.width * self.height
    
    def getWidth(self):
        self.width = width

    def getHeight(self):
        self.height = height

def main():
    # create first rectangle
    rectangle1 = Rectangle(4,40)
    print("Rectangle 1")
    print("Width:",rectangle1.width)
    print("Height:",rectangle1.height)
    print("Area:",rectangle1.getArea())
    print("Perimeter:",rectangle1.getPerimeter())

    print()

    # create second rectangle
    rectangle2 = Rectangle(3.5,35.7)
    print("Rectangle 2")
    print("Width:",rectangle2.width)
    print("Height:",rectangle2.height)
    print("Area:",rectangle2.getArea())
    print("Perimeter:",rectangle2.getPerimeter())
          
main()
