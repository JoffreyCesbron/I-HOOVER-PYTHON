from unittest import TestCase

from Commands import Commands


class TestCommands(TestCase):

    def test_error_commands(self):
        # Given
        commands = "Z"

        # Then
        self.assertRaises(ValueError, Commands, commands)

    def test_commands_ok(self):
        # Given
        commands = "DGGA"

        # Then
        self.assertTrue(Commands(commands).values == "DGGA")
