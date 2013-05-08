#!/usr/bin/env python

"""
circle class -- 

basic skeleton: fill in with properties..

Write a Circle class with decorator syntax for properties:
  instantiate with a radius: c = Circle(4)

Use a property for the diameter: get and settable:
    d = c.diameter
    c.diameter = 5

use a property for the area: only gettable
    a = c.area
    a.area = 5 => AttributeError

add methods so that str(circle) and repr(circle)
    produce something reasonable.

extra credit: make it so you can add two circles:

>>> Circle(2) + Circle(3)
Circle(5.000000)


see test_circle_properties.y for requirements.

"""

import math


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)

    @staticmethod
    def circumference(radius):
        return 2 * math.pi * radius

    @property
    def diameter(self):
        """I'm the diameter property"""
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def area(self):
        return math.pi * self.radius**2

    def __add__(self, circle):
        return Circle(self.radius + circle.radius)

    def __repr__(self):
        return "Circle(%f)" % self.radius

    def __str__(self):
        return "Circle Object with radius: %f" % self.radius

if __name__ == '__main__':
    c = Circle(5)
    print c.diameter
    print c.radius
    print 'area: %s' % c.area

    print str(c)
    # put the rest in here...