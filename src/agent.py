class Agent:
    def __init__(self, id, strategy, memory=None):
        self.id = id
        self.strategy = strategy
        self.memory = memory if memory is not None else {}  # Using a dictionary for detailed memory

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

        if self.strategy == 'complex-strategy':
            return self.complex_decision(opponent)

        # Default behavior
        return 'C'

    def update_memory(self, opponent, my_decision, their_decision, outcome):
        if opponent.id not in self.memory:
            self.memory[opponent.id] = []

        self.memory[opponent.id].append({
            'my_decision': my_decision,
            'their_decision': their_decision,
            'outcome': outcome
        })

    def complex_decision(self, opponent):
        # Analyze past interactions from memory to make a decision
        # Example: If opponent defected in most recent interaction, defect
        if opponent.id in self.memory and self.memory[opponent.id][-1]['their_decision'] == 'D':
            return 'D'
        return 'C'

