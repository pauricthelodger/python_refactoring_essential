import unittest

from comments.src.X1 import X1


class TestX1(unittest.TestCase):

    def test_n_basic(self):
        self.assertEqual(X1.square(0), 0)
        self.assertEqual(X1.square(2), 4)
        self.assertEqual(X1.square(-3), 9)

    def test_m_single_value(self):
        self.assertEqual(X1.sum_of_squares(3, 3), 9)

    def test_m_small_range(self):
        self.assertEqual(X1.sum_of_squares(1, 3), 14)

    def test_m_larger_range(self):
        self.assertEqual(X1.sum_of_squares(0, 3), 14)

    def test_m_negative_range(self):
        self.assertEqual(X1.sum_of_squares(-2, 0), 5)

    def test_m_larger_negative_to_positive(self):
        self.assertEqual(X1.sum_of_squares(-1, 1), 2)


if __name__ == "__main__":
    unittest.main()
