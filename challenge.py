import math


def square_area(side):
    """Returns the area of a square"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return side**2


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return base * height


def triangle_area(base, height):
    """Returns the area of a triangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (base * height)/2


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (diagonal_1 * diagonal_2)/2


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return ((base_major + base_minor)/2)*height


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (perimeter*apothem)/2


def circumference_area(radius):
    """Returns the area of a circumference"""
    # You have to code here
    # REMEMBER: Tests first!!!
    # Use math.pi for π value
    return round(math.pi * radius**2,2)


if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            # Initialize the needed values for the tests
            self.square = {
                4:2,
                9:3,
                16:4,
                25:5,
                36:6
            }
            self.rectangle = {
                8:[2, 4],
                16:[2, 8],
                32:[8, 4],
                72:[36, 2],
                46:[23, 2],
                102:[51, 2]

           }
            self.triangle = {
                4:[2, 4],
                18:[9, 4],
                10.5:[3, 7],
                24.5:[7, 7],
                15:[5, 6]
            }
            self.rhombus = {
                32 : [8,8],
                36 : [12,6],
                12 : [8,3]
            }

            self.trapezoid = {
                12: [5,7,2],
                40: [12,4,5],
                102: [22,12,6]

            }

            self.polygon = {
                15: [10,3],
                48: [24,4],
               168: [56,6] 
            }

            self.circumference = {
                78.54: 5,
               201.06: 8,
                28.27: 3
            }


        def test_square_area(self):
            for key, value in self.square.items():
                self.assertEqual(key, square_area(value))

        def test_rectangle_area(self):
            for key, value in self.rectangle.items():
                self.assertEqual(key,rectangle_area(value[0],value[1]))

        def test_triangle_area(self):
            for key, value in self.triangle.items():
                self.assertEqual(key,triangle_area(value[0],value[1]))

        def test_rhombus_area(self):
            for key, value in self.rhombus.items():
                self.assertEqual(key,rhombus_area(value[0],value[1]))

        def test_trapezoid_area(self):
            for key, value in self.trapezoid.items():
                self.assertEqual(key,trapezoid_area(value[0],value[1],value[2]))

        def test_regular_polygon_area(self):
            for key, value in self.polygon.items():
                self.assertEqual(key,regular_polygon_area(value[0],value[1]))

        def test_circumference_area(self):
            for key, value in self.circumference.items():
                self.assertEqual(key,circumference_area(value))

        def tearDown(self):
            del(self.square)
            del(self.rectangle)
            del(self.triangle)
            del(self.rhombus)
            del(self.trapezoid)
            del(self.polygon)
            del(self.circumference)

    unittest.main()
