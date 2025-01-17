
import pytest
import numpy as np
from numpy.testing import assert_equal
from fractions import Fraction
from ufunclab import cross3, cross2


@pytest.mark.parametrize('u, v', [([1, 2, 3], [5, 3, 1]),
                                  ([1.5, 0.5, -1.5], [2.0, 9.0, -3.0]),
                                  ([1+2j, 3, -4j], [3-1j, 2j, 6])])
def test_cross3_basic(u, v):
    w = cross3(u, v)
    assert_equal(w, np.cross(u, v))


def test_cross3_object1():
    u = np.array([1, 2-1j, Fraction(1, 2)], dtype=object)
    v = np.array([-2.5, 8, Fraction(3, 2)], dtype=object)
    w = cross3(u, v)
    assert w.dtype == np.dtype(object)
    assert_equal(w, np.array([-1-1.5j, -2.75, 13-2.5j], dtype=object))


def test_cross3_object2():
    u = np.array([1, 2+1j, -2], dtype=object)
    v = np.array([5, -3j, Fraction(1, 2)], dtype=object)
    w = cross3(u, v)
    assert w.dtype == np.dtype(object)
    assert_equal(w, np.array([1-5.5j, Fraction(-21, 2), -10-8j], dtype=object))


def test_cross3_basic_broadcasting():
    u = np.arange(21).reshape(7, 1, 3)
    v = -0.5*np.arange(15).reshape(1, 5, 3)
    w = cross3(u, v)
    assert_equal(w, np.cross(u, v))


def test_cross3_nontrivial_axes():
    u = np.arange(12).reshape(4, 3, 1)
    v = np.arange(6).reshape(3, 1, 2)
    w = cross3(u, v, axes=[1, 0, 2])
    assert_equal(w, np.cross(u, v, axisa=1, axisb=0, axisc=2))


@pytest.mark.parametrize('u, v', [([1, 2], [5, 3]),
                                  ([1.5, 0.5], [2.0, 9.0]),
                                  ([1+2j, 3], [3-1j, 2j])])
def test_cross2_basic(u, v):
    w = cross2(u, v)
    assert_equal(w, np.cross(u, v))


def test_cross2_broadcasting():
    x = np.arange(70).reshape(7, 2, 5)
    y = np.arange(10).reshape(5, 2)
    z = cross2(x, y, axes=[(1,), (1,)])
    assert_equal(z, np.cross(x, y, axisa=1, axisb=1))


def test_cross2_object():
    u = np.array([Fraction(2, 3), Fraction(1, 5)])
    v = np.array([[Fraction(3, 2), Fraction(3, 5)], [8, 9]])
    w = cross2(u, v)
    expected = np.array([Fraction(1, 10), Fraction(22, 5)])
    assert w.dtype == np.dtype(object)
    assert_equal(w, expected)
