import unittest
import numpy as np


class TestInput(unittest.TestCase):
    def setUp(self):
        self.data = np.genfromtxt('dataset.csv', delimiter=',')

    def test_shape(self):
        self.assertEqual(16, self.data.shape[1], "wrong length of the array")

    def test_normalized(self):
        for column in self.data.T:
            self.assertEqual(0, np.round(np.std(column)), "data is not normalized, std != 0")
            self.assertTrue(0 <= np.mean(column) <= 1, "data is not normalized, mean is out of range(0, 1)")

    def test_type(self):
        self.assertEqual(np.ndarray, type(self.data), "wrong type of data")
        self.assertEqual(np.float64, type(self.data[0, 0]), "wrong type of data")


if __name__ == '__main__':
    unittest.main()
