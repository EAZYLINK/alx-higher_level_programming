#!/usr/bin/python3

"""Define a class Rectangle"""

class Rectangle:
    """A Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialize a Rectangle.

        Args:
            width (int): The of the rectangle.
            height (int): The height of the rectangle."""
            self.width = width
            self.height = height
        
        @property
        def width(self):
            """Get/set the width of the rectangle."""
            return self._width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raie TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self._width = value

        @property
        def height(self):
            """Get/set the height of the rectangle."""
            return self._width

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raie TypeError("heigth must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self._heigth = value

