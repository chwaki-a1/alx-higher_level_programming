#!/usr/bin/python3
"""
Module for a class that prevents dynamic creation of attributes
"""


class LockedClass():
    """Class to prevent dynamic attributes creation"""
    __slots__ = ['first_name']

    def __init__(self):
        """Init method"""
        pass
