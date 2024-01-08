import networkx as nx
from agent import Agent

def create_network():
    network = nx.Graph()
    agents = [Agent(id=i, strategy='cooperate' if i % 2 == 0 else 'defect') for i in range(10)]

    for agent in agents:
        network.add_node(agent)

    # Future: Add edges and weights
    return agents
