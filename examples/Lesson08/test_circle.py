"""
tests for Circle class
"""

import math

from circle import Circle


def test_create_from_radius():
    c = Circle(4)

    assert c.radius == 4


def test_change_radius():
    c = Circle(4)

    c.radius = 10
    assert c.radius == 10


def test_diameter():
    c = Circle(4)

    assert c.diameter == 8


def test_change_radius_get_diameter():
    c = Circle(4)

    c.radius = 6

    assert c.diameter == 12


def test_set_diameter():
    c = Circle(4)

    c.diameter = 6

    assert c.radius == 3


def test_area():
    c = Circle(2)
    print(c.area)

    assert c.area == 4 * math.pi

