from game import run_game
from network import create_network, update_network_weights

def main():
    network, agents = create_network(num_agents=10)

    # Run the game for a specified number of iterations
    for iteration in range(10):
        print(f"Running iteration {iteration + 1}")
        outcomes = run_game(agents)

        # Update network weights based on game outcomes
        for outcome in outcomes:
            agent1, agent2, result = outcome
            update_network_weights(network, agent1, agent2, result)

    print("Simulation complete.")

if __name__ == "__main__":
    main()
