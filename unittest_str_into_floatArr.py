import unittest
from str_into_floatArr import str_into_floatArr

class TestStrIntoFloatArr(unittest.TestCase):
    """ Tests function str_into_floatArr """
    def test1(self):
        s = "100    12 0.301 -4.12\n"
        self.assertEqual(str_into_floatArr(s, 4),
                        [100, 12, 0.301, -4.12])

if __name__ == "__main__":
    unittest.main()
