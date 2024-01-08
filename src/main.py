from game import run_game
from network import create_network
from agent import Agent

def main():
    # Create a network of agents
    agents = create_network()

    # Run the game for a specified number of iterations
    for _ in range(100):  # Example: 100 iterations
        run_game(agents)

    print("Simulation complete.")

if __name__ == "__main__":
    main()
