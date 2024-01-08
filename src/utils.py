import unittest
from agent import Agent
from game import run_game

class TestGame(unittest.TestCase):
    def test_game_outcome(self):
        agents = [Agent(id=1, strategy='cooperate'), Agent(id=2, strategy='defect')]
        # Future implementation: Test for correct game outcomes

if __name__ == '__main__':
    unittest.main()
