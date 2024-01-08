def calculate_score(decision1, decision2):
    if decision1 == 'C' and decision2 == 'C':
        return (3, 3)  # Both cooperate
    elif decision1 == 'C' and decision2 == 'D':
        return (0, 5)  # Agent1 cooperates, Agent2 defects
    # Add other scenarios
    else:
        return (5, 0)  # Agent1 defects, Agent2 cooperates
    

def run_game(agents):
    outcomes = []
    for i in range(0, len(agents), 2):
        agent1 = agents[i]
        agent2 = agents[i + 1]

        decision1 = agent1.decide(agent2)
        decision2 = agent2.decide(agent1)

        score1, score2 = calculate_score(decision1, decision2)
        # Update agents' scores and record results (example: using 'mutual_cooperation' as outcome)
        outcome = 'mutual_cooperation' if decision1 == 'C' and decision2 == 'C' else 'defection'
        outcomes.append((agent1, agent2, outcome))

         # Print decisions (expand to include scoring) 
        print(f"Agent {agent1.id} ({agent1.strategy}) vs Agent {agent2.id} ({agent2.strategy}): {decision1} vs {decision2}, scores: ({score1},{score2})")

    return outcomes