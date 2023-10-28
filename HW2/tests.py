import unittest
import math
from contrived_func import contrived_func


class TestHW2(unittest.TestCase):
    def test1(self):
        result = contrived_func(22)  # passing c13, 23, 28
        print(result)

    def test2(self):
        result = contrived_func(25)
        print(result)  # passing c21, c9

    def test3(self):
        result = contrived_func(7)
        print(result)  # passing c18, 25, 3

    def test4(self):
        result = contrived_func(19)
        print(result)  # passing c11, 22, 23, 28

    def test5(self):
        result = contrived_func(2)
        print(result)  # passing c20

    def test6(self):
        result = contrived_func(-15)
        print(result)  # passing c18, 25, 4

    def test7(self):
        result = contrived_func(10)
        print(result)  # passing c15, 24, 28

    def test8(self):
        result = contrived_func(-4)
        print(result)  # passing c20, c26, c8


if __name__ == "__main__":
    unittest.main()
