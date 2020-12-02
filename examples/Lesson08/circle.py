"""
class for a full featured circle
"""

import math

print("import the new one")

class Circle:

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return (self.diameter / 2)**2 * math.pi

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2



