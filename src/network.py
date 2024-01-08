import networkx as nx
from agent import Agent

def create_network():
    network = nx.Graph()
    agents = [Agent(id=i, strategy='cooperate' if i % 2 == 0 else 'defect') for i in range(10)]

    for agent in agents:
        network.add_node(agent)

    # Add edges to form a network
    # Example: Connect each agent to its neighbors
    for i in range(len(agents)):
        network.add_edge(agents[i], agents[(i + 1) % len(agents)])

    # Future: Add edges and weights
    return agents

