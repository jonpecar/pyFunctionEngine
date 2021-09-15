import unittest

from FunctionEngine.FunctionEngine import Term
from FunctionEngine.Functions import *

import numpy as np

class arithmeticTests(unittest.TestCase):

    def test_add(self):
        a = 1.23456
        b = 9.87654

        self.assertEqual((Term(a) + b).magnitude, a + b)
        self.assertEqual((a + Term(b)).magnitude, a + b)
        self.assertEqual((Term(a) + Term(b)).magnitude, a + b)

    def test_subtract(self):
        a = 1.23456
        b = 9.87654

        self.assertEqual((Term(a) - b).magnitude, a - b)
        self.assertEqual((a - Term(b)).magnitude, a - b)
        self.assertEqual((Term(a) - Term(b)).magnitude, a - b)

    def test_multiply(self):
        a = 1.23456
        b = 9.87654

        self.assertEqual((Term(a) * b).magnitude, a * b)
        self.assertEqual((a * Term(b)).magnitude, a * b)
        self.assertEqual((Term(a) * Term(b)).magnitude, a * b)

    def test_div(self):
        a = 1.23456
        b = 9.87654

        self.assertEqual((Term(a) / b).magnitude, a / b)
        self.assertEqual((a / Term(b)).magnitude, a / b)
        self.assertEqual((Term(a) / Term(b)).magnitude, a / b)

    def test_pow(self):
        a = 1.23456
        b = 9.87654

        self.assertEqual((Term(a) ** b).magnitude, a ** b)
        self.assertEqual((a ** Term(b)).magnitude, a ** b)
        self.assertEqual((Term(a) ** Term(b)).magnitude, a ** b)

    def test_cos(self):
        a = 1.23456

        self.assertEqual((cos(Term(a))).magnitude, np.cos(a))
        self.assertEqual((cos(a)).magnitude, np.cos(a))

    
    def test_tan(self):
        a = 1.23456

        self.assertEqual((tan(Term(a))).magnitude, np.tan(a))
        self.assertEqual((tan(a)).magnitude, np.tan(a))

    
    def test_sin(self):
        a = 1.23456

        self.assertEqual((sin(Term(a))).magnitude, np.sin(a))
        self.assertEqual((sin(a)).magnitude, np.sin(a))


    def test_acos(self):
        a = 0.123456

        self.assertEqual((acos(Term(a))).magnitude, np.arccos(a))
        self.assertEqual((acos(a)).magnitude, np.arccos(a))

    
    def test_atan(self):
        a = 1.23456

        self.assertEqual((atan(Term(a))).magnitude, np.arctan(a))
        self.assertEqual((atan(a)).magnitude, np.arctan(a))

    
    def test_asin(self):
        a = 0.123456

        self.assertEqual((asin(Term(a))).magnitude, np.arcsin(a))
        self.assertEqual((asin(a)).magnitude, np.arcsin(a))

    def test_sqrt(self):
        a = 2

        self.assertEqual((sqrt(Term(a))).magnitude, a**0.5)
        self.assertEqual((sqrt(a)).magnitude, a**0.5)

