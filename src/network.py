import networkx as nx
from agent import Agent

def create_network():
    # Example: Create a simple network of 10 agents
    network = nx.Graph()
    agents = [Agent(id=i, strategy='cooperate') for i in range(10)]

    # Add agents as nodes
    for agent in agents:
        network.add_node(agent)

    # Future implementation: Add edges and weights
    return agents
