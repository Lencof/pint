# -*- coding: utf-8 -*-
"""
    pint.converters
    ~~~~~~~~~

    Functions and classes related to unit conversions.

    :copyright: 2016 by Pint Authors, see AUTHORS for more details.
    :license: BSD, see LICENSE for more details.
"""
from __future__ import (division, unicode_literals, print_function,
                        absolute_import)

# create class Converter(object):
class Converter(object):
    """Base class for value converters.
    """

    is_multiplicative = True

    # create def to_reference(self, value, inplace=False):
    def to_reference(self, value, inplace=False):
        return value

    # create def from_reference(self, value, inplace=False):
    def from_reference(self, value, inplace=False):
        return value


# create class ScaleConverter(Converter):
class ScaleConverter(Converter):
    """A linear transformation
    """

    is_multiplicative = True

    # create def __init__(self, scale):
    def __init__(self, scale):
        self.scale = scale

    # create def to_reference(self, value, inplace=False):
    def to_reference(self, value, inplace=False):
        if inplace:
            value *= self.scale
        else:
            value = value * self.scale

        return value

    # create def from_reference(self, value, inplace=False):
    def from_reference(self, value, inplace=False):
        if inplace:
            value /= self.scale
        else:
            value = value / self.scale

        return value

# create class OffsetConverter(Converter):
class OffsetConverter(Converter):
    """An affine transformation
    """

    # create def __init__(self, scale, offset):
    def __init__(self, scale, offset):
        self.scale = scale
        self.offset = offset

    # create @property
    @property
    def is_multiplicative(self):
        return self.offset == 0

    # create def to_reference(self, value, inplace=False):
    def to_reference(self, value, inplace=False):
        if inplace:
            value *= self.scale
            value += self.offset
        else:
            value = value * self.scale + self.offset

        return value 

    # create def from_reference(self, value, inplace=False):
    def from_reference(self, value, inplace=False):
        if inplace:
            value -= self.offset
            value /= self.scale
        else:
            value = (value - self.offset) / self.scale

        return value
