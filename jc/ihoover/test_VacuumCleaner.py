from unittest import TestCase

from VacuumCleaner import VacuumCleaner


class TestVaccumCleaner(TestCase):

    def test_error_orientation_constructor(self):
        # Given
        x = 1
        y = 10
        orientation = "aaa"

        # Then
        self.assertRaises(ValueError, VacuumCleaner, x, y, orientation)

    def test_error_x_constructor(self):
        # Given
        x = -1
        y = 10
        orientation = "N"

        # Then
        self.assertRaises(ValueError, VacuumCleaner, x, y, orientation)

    def test_vaccum_cleaner_constructor_is_ok(self):
        # Given
        x = 1
        y = 10
        orientation = "N"

        # Then
        self.assertTrue(VacuumCleaner(1, 10, orientation).orientation == orientation)
