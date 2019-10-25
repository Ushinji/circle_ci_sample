import unittest
from sum import sum


class TestSum(unittest.TestCase):
    def test_sum(self):
        assert sum(1, 2) == 3
