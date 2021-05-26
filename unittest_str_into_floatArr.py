 import unittest
 from str_into_floatArr import str_into_floatArr

 class TestStrIntoFloatArr(unittest.TestCase):
    def setUp(self):
        self.str_into_floatArr = str_into_floatArr(s, size)

    def test1(self):
        self.assertEqual(self.str_into_floatArr('100    12 0.301 -4.12 471 ', 4),
        [100; 12; 0.301; -4.12])

if __name__ == "__main__":
    unittest.main()
