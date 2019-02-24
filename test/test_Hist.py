import unittest
from src.Hist import *

class TestHist(unittest.TestCase):
    def setUp(self):
        self.v = [1, 2, 2, 3, 3, 3, 4, 4 ,4, 4]

    def test_init_createHistWithProperElements(self):
        h = Hist(self.v)

        self.assertEqual(len(h.d), 4)
        self.assertEqual(h.total(), len(self.v))

    def test_getitem_returnCorrectItem(self):
        h = Hist(self.v)

        self.assertEqual(h[1], 1)
        self.assertEqual(h[2], 2)
        self.assertEqual(h[3], 3)
        self.assertEqual(h[4], 4)

    def test_freq_returnFrequencyOfItem(self):
        h = Hist(self.v)

        self.assertEqual(h.freq(1), 1)
        self.assertEqual(h.freq(2), 2)
        self.assertEqual(h.freq(3), 3)
        self.assertEqual(h.freq(4), 4)
    
    def test_freq_returnZeroWhenItemDoesNotExist(self):
        h = Hist(self.v)        

        self.assertEqual(h.freq(-1), 0)

    def test_Total_returnsCountOfElementsInHistogram(self):
        h = Hist(self.v)

        self.assertEqual(h.total(), len(self.v))

    def test_x_y_retunsValuesOfAxes(self):
        h = Hist(self.v)
        x = [1, 2, 3, 4]
        y = [1, 2, 3, 4]

        xh, yh = h.x_y()

        self.assertEqual(xh, x)
        self.assertEqual(yh, y)

if __name__ == "__main__":
    unittest.main()