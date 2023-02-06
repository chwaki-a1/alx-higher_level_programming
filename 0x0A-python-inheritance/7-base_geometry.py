#!/usr/bin/python3

"""
    This module contains a class BaseGeometry
"""


class BaseGeometry:

    """This class contains methods that raises exception and validates value"""

    def area(self):

        """Raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """
        Validates an integer

        Args:
            name: must be a string
            value: must be an integer and > 0

        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
