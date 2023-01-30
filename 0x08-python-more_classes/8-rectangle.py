#!/usr/bin/python3

"""

A rectangle with width and height.

"""


class Rectangle:
    """
    Rectangle functions and data
    """

    # Public
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        """ Instantiation
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):

        """ Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):

        """ Setter for width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        """ Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):

        """ Setter for height
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # Functions
    def area(self):

        """ Returns area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):

        """ Returns perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        """ Returns whichever is bigger, rect_1 or rect_2
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):

        """ print() __str__ method funtion to return rectangle in char '#'
        """
        res = ""
        if self.__width == 0 or self.__height == 0:
            return res

        for i in range(self.__height):
            for i2 in range(self.__width):
                res += str(self.print_symbol)
            if i != self.__height - 1:
                res += '\n'
        return res

    def __repr__(self):

        """ print() or eval() __repr__ method function to return
            ... Rectangle(width, height)
        """
        w = str(self.__width)
        h = str(self.__height)

        res = "Rectangle(" + w + ", " + h + ")"
        return res

    def __del__(self):
        """ Print a message for del
            Decrement instance when del is called
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
