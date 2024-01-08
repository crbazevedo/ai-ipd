import unittest
from agent import Agent

class TestAgent(unittest.TestCase):
    def test_agent_creation(self):
        agent = Agent(id=1, strategy='cooperate')
        self.assertEqual(agent.id, 1)
        self.assertEqual(agent.strategy, 'cooperate')

if __name__ == '__main__':
    unittest.main()
