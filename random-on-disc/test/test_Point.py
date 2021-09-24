import unittest

from Point import Point


class TestPoint(unittest.TestCase):

    def testDistance(self):

        self.assertEqual(Point(0, 0).distance(Point(0, 0)), 0)
        self.assertEqual(Point(0, 0).distance(Point(1, 0)), 1)
        self.assertAlmostEqual(Point(0, 0).distance(Point(1, 1)), 1.414, 3)

        self.assertEqual(Point(0, 0).distance(Point(3, 4)), 5)
