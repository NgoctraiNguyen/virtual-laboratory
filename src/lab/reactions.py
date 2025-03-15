class Reaction:
    def __init__(self):
        self.reactions = {}

    def add_reaction(self, chemical1, chemical2, result):
        self.reactions[(chemical1, chemical2)] = result

    def mix(self, chemical1, chemical2):
        if (chemical1, chemical2) in self.reactions:
            return self.reactions[(chemical1, chemical2)]
        elif (chemical2, chemical1) in self.reactions:
            return self.reactions[(chemical2, chemical1)]
        else:
            return "No reaction occurs."

    def simulate_reaction(self, chemical1, chemical2):
        outcome = self.mix(chemical1, chemical2)
        # Here you could add additional logic for simulating the reaction process
        return outcome