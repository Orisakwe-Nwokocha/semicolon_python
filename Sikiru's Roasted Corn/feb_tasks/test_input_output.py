import unittest

from input_output import InputOutput


class TestInputOutput(unittest.TestCase):
    def test_input_hello_world_output_HELLO_WORLD(self):
        input_output = InputOutput()

        input_output.get_string("")
        self.assertEqual("HELLO WORLD", input_output.print_string())

