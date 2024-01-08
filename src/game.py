def run_game(agents):
    # Pair agents and run a round
    for i in range(0, len(agents), 2):
        agent1 = agents[i]
        agent2 = agents[i + 1]

        decision1 = agent1.decide(agent2)
        decision2 = agent2.decide(agent1)

        # Example: Print decisions (expand to include scoring)
        print(f"Agent {agent1.id} ({agent1.strategy}) vs Agent {agent2.id} ({agent2.strategy}): {decision1} vs {decision2}")
