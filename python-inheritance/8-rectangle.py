#!/usr/bin/python3
'''8. Rectangle'''


class BaseGeometry:
    '''class BaseGeometry (based on 7-base_geometry.py)'''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int) or type(value) is bool:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    '''class Rectangle that inherits from BaseGeometry (7-base_geometry.py)'''


    def __init__(self, width, height):
        '''initialization of the class'''
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

    def area(self):
        '''returns the area of the rectangle'''
        return self.__width * self.__height
