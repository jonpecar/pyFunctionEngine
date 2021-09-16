import pytest

from FunctionEngine.FunctionEngine import Term
from FunctionEngine.Functions import *

import numpy as np

def test_add():
    a = 1.23456
    b = 9.87654

    assert (Term(a) + b).magnitude == a + b
    assert (a + Term(b)).magnitude== a + b
    assert (Term(a) + Term(b)).magnitude== a + b

def test_subtract():
    a = 1.23456
    b = 9.87654

    assert (Term(a) - b).magnitude== a - b
    assert (a - Term(b)).magnitude== a - b
    assert (Term(a) - Term(b)).magnitude== a - b

def test_multiply():
    a = 1.23456
    b = 9.87654

    assert (Term(a) * b).magnitude== a * b
    assert (a * Term(b)).magnitude== a * b
    assert (Term(a) * Term(b)).magnitude== a * b

def test_div():
    a = 1.23456
    b = 9.87654

    assert (Term(a) / b).magnitude== a / b
    assert (a / Term(b)).magnitude== a / b
    assert (Term(a) / Term(b)).magnitude== a / b

def test_pow():
    a = 1.23456
    b = 9.87654

    assert (Term(a) ** b).magnitude== a ** b
    assert (a ** Term(b)).magnitude== a ** b
    assert (Term(a) ** Term(b)).magnitude== a ** b


def test_sqrt():
    a = 2

    assert (sqrt(Term(a))).magnitude== a**0.5
    assert (sqrt(a)).magnitude== a**0.5


def test_cos():
    a = 1.23456

    assert (cos(Term(a))).magnitude== np.cos(a)
    assert (cos(a)).magnitude== np.cos(a)


def test_tan():
    a = 1.23456

    assert (tan(Term(a))).magnitude== np.tan(a)
    assert (tan(a)).magnitude== np.tan(a)


def test_sin():
    a = 1.23456

    assert (sin(Term(a))).magnitude== np.sin(a)
    assert (sin(a)).magnitude== np.sin(a)


def test_acos():
    a = 0.123456

    assert (acos(Term(a))).magnitude== np.arccos(a)
    assert (acos(a)).magnitude== np.arccos(a)


def test_atan():
    a = 1.23456

    assert (atan(Term(a))).magnitude== np.arctan(a)
    assert (atan(a)).magnitude== np.arctan(a)


def test_asin():
    a = 0.123456

    assert (asin(Term(a))).magnitude== np.arcsin(a)
    assert (asin(a)).magnitude== np.arcsin(a)


