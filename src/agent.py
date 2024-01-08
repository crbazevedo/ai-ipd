class Agent:
    def __init__(self, id, strategy):
        self.id = id
        self.strategy = strategy

    def decide(self, opponent):
        if self.strategy == 'cooperate':
            return 'C'
        elif self.strategy == 'defect':
            return 'D'
        else:
            # Future implementation: More complex strategies
            return 'C'
