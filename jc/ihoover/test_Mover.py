from unittest import TestCase

from Mover import *


class Test(TestCase):

    def orientation_w_and_move_to_the_right(self):
        # Given
        vacuumCleaner = VacuumCleaner(1, 1, "W")
        output = orientate_to_the_right(vacuumCleaner).orientation

        # Then
        self.assert_(output == 'N')
