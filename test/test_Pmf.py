import unittest
from src.Pmf import *

class TestPmf(unittest.TestCase):
    def setUp(self):
        self.v = [1, 2, 2, 3, 3, 3, 4, 4 ,4, 4]

    def test_init_InitializeElements(self):
        pmf = Pmf(self.v)

        self.assertEqual(len(pmf.d), 4)

    def test_init_NormalizeElements(self):
        pmf = Pmf(self.v)
        pmf.normalize()        

        y = pmf.x_y()[1]

        self.assertEqual(sum(y), 1)

    def test_x_y_retunsValuesOfAxes(self):
        x = [1, 2, 3, 4]
        y = [1, 2, 3, 4]
        s = sum(y)
        fct = 1.0/s
        y = [fct * i for i in y]

        pmf = Pmf(self.v)
        pmf.normalize()

        xp, yp = pmf.x_y()

        self.assertEqual(xp, x)
        self.assertEqual(yp, y)
        