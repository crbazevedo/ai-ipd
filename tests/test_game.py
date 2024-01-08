import unittest
from game import calculate_score

class TestGame(unittest.TestCase):
    def test_score_calculation(self):
        self.assertEqual(calculate_score('C', 'C'), (3, 3))
        # Other scenarios
