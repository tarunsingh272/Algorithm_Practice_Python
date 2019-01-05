import unittest

def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError()
    if x > 0:
        return x
    elif x <= 0:
        return -1 * x


class TestAbs(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(my_abs(1),1)
    def test_negative(self):
        self.assertEqual(my_abs(-1),1)
    def test_type(self):
        with self.assertRaises(TypeError):
            my_abs('AAA')
