import unittest
from moving_average import *


class UnittestOfProgram(unittest.TestCase):
    def test_addSample(self):
        module = MovingAverage(1000)
        for i in range(1000):
            module.addSample(i)
        self.assertEqual(module.addSample(25)[-1], module.samples[-1])

    def test_addSample_removing_first(self):
        module = MovingAverage(250)
        for i in range(250):
            module.addSample(i)
        module.addSample(25)
        self.assertEqual(module.samples[0], 1)

    def test_getAverage_overLimit(self):
        module = MovingAverage(25)
        for i in range(500):
            module.addSample(i)
        self.assertEqual(module.getAverage(), 487)

    def test_getAverage_underLimit(self):
        a = []
        module = MovingAverage(500)
        for i in range(250):
            module.addSample(i)
            a.append(i)
            facit = sum(a)/250
        self.assertEqual(module.getAverage(), facit)


if __name__ == "__main__":
    unittest.main()


