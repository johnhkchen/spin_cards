# Tests for the main module
# Path: tests\test_main.py

import unittest
from main import main


class MyTestCase(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), 0)


if __name__ == "__main__":
    unittest.main()
