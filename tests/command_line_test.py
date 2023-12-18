from unittest import TestCase
from imagefix.command_line import main


class TestConsole(TestCase):
    def test_basic(self):
        main()
