class Agent:
    def __init__(self, id, strategy, memory=[]):
        self.id = id
        self.strategy = strategy
        self.memory = memory  # For remembering past interactions

    def decide(self, opponent):
        if self.strategy == 'tit-for-tat':
            if not self.memory or self.memory[-1][opponent.id] == 'C':
                return 'C'  # Cooperate if no memory or last interaction was cooperation
            else:
                return 'D'  # Defect if last interaction was defection
        elif self.strategy == 'always-cooperate':
            return 'C'
        elif self.strategy == 'always-defect':
            return 'D'
        # Additional strategies can be added here

    def update_memory(self, opponent, their_decision):
        # Update the agent's memory about the opponent's last decision
        if opponent.id not in self.memory:
            self.memory[opponent.id] = []
        self.memory[opponent.id].append(their_decision)
