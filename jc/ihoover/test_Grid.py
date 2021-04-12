from unittest import TestCase
from Grid import Grid


class TestGrid(TestCase):

    def test_error_x_constructor(self):
        # Given
        max_x = -1
        max_y = 10

        # Then
        self.assertRaises(ValueError, Grid, max_x, max_y)

    def test_error_y_constructor(self):
        # Given
        max_x = 1
        max_y = 0

        # Then
        self.assertRaises(ValueError, Grid, max_x, max_y)

    def test_grid_constructor_is_ok(self):
        # Given
        max_x = 10
        max_y = 10

        # Then
        self.assertTrue(Grid(max_x, max_y).max_x == max_x)
