#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yuande Liu <miraclecome (at) gmail.com>

from __future__ import print_function, division

class Rational(object):
    """ Usage:

        >>> a = Rational(3, 4)
        >>> b = Rational(1, 3)
        >>> c = a + b
        >>> print(c)
    """

    def __init__(self, numerator, denominator):
        if denominator == 0: raise
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, obj):
        """ override + of the object
            c = a + b -> a .+ b -> a.__add__(b)
            doing gcd in __add__ rather than __str__,
            because language like c don't have high-precision number like python
        """
        _numerator = self.numerator * obj.denominator + obj.numerator * self.denominator
        _denominator = self.denominator * obj.denominator
        ret = self.gcd(_numerator, _denominator)
        self.numerator = _numerator // ret
        self.denominator = _denominator // ret
        return self

    def __str__(self):
        ret = self.gcd(self.numerator, self.denominator)
        
        if self.denominator // ret == 1:
            return '{}'.format(self.numerator // ret)
        return '{}/{}'.format(self.numerator, self.denominator)

    def gcd(self, m, n):
        """ m, n get absoluate value
        """
        if m < 0: m *= -1
        if n < 0: n *= -1
        border = n if m > n else m
        for i in range(border, 0, -1):
            if m % i == n % i == 0:
                return i

if __name__ == '__main__':
    a = Rational(3, 4)
    b = Rational(1, 3)
    c = a + b
    print(c)

