#!/usr/bin/env python

"""
nifty Circle class

Used to demo propeties and "magic methods"
"""

from math import pi
import functools


# this is a trick to make all the greater than, less than, etc work.
# see: https://docs.python.org/3/library/functools.html#functools.total_ordering
@functools.total_ordering
class Circle(object):
    """
    simple class to represent a circle

    One you can do math with -- a bit odd...
    """

    def __init__(self, radius):
        """
        Create a new Circle

        :param radius: the radius of the circle
        """

        self.radius = float(radius)

    @classmethod
    def from_diameter(cls, diameter):
        """
        Create a new Circle

        :param diameter: the diameter of the circle
        """

        return cls(diameter / 2.0)

    @property
    def diameter(self):
        """
        The diameter of the circle
        """
        return self.radius * 2.0
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2.0

    @property
    def area(self):
        """
        The area of the circle
        """
        return self.radius**2 * pi

    def __repr__(self):
        # using the repr (!r) formatter is a neat trick
        # return "Circle({!r})".format(self.radius)
        return f"Circle({self.radius!r})"

    def __str__(self):
        # return "Circle with radius: {:g}".format(self.radius)
        return f"Circle with radius: {self.radius:g}"

    @staticmethod
    def sort_key(a_circle):
        """
        sort_key that makes it easy to sort Circles
        """
        return a_circle.radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __iadd__(self, other):
        """
        for "augmented assignment" -- can be used for in-place addition

        Generally used this way for mutable types. This approach returns
        self, so that the object is changed in place -- i.e. mutated
        """
        self.radius += other.radius
        return self

    def __mul__(self, factor):
        return Circle(self.radius * factor)

    def __imul__(self, factor):
        """see __iadd__"""
        self.radius *= factor
        return self

    def __rmul__(self, factor):
        return Circle(self.radius * factor)

    # You can define them all:
    #  Might be useful for odd situations (and better performance)
    # def __eq__(self, other):
    #     return self.radius == other.radius
    # def __ne__(self, other):
    #     return self.radius != other.radius
    # def __gt__(self, other):
    #     return self.radius > other.radius
    # def __ge__(self, other):
    #     return self.radius >= other.radius
    # def __lt__(self, other):
    #     return self.radius < other.radius
    # def __le__(self, other):
    #     return self.radius <= other.radius

    # Or you can put the @total_ordering decorator on the class definition
    # and do only these:
    def __eq__(self, other):
        try:
            return self.radius == other.radius
        except AttributeError:
            return NotImplemented

    def __lt__(self, other):
        try:
            return self.radius < other.radius
        except AttributeError:
            return NotImplemented


# This demonstrates how you can
#  subclass and get everything from circle
#     -- even the alternate constructor!
class Sphere(Circle):
    """
    A simple Sphere object, which you can do math with...
    """

    def volume(self):
        return 4 / 3 * pi * self.radius ** 3

    @property
    def area(self):
        return 4 * pi * self.radius ** 2

    def __repr__(self):
        return "Sphere({:g})".format(self.radius)

    def __str__(self):
        return "Sphere with radius: {:g}".format(self.radius)

