class Chemical:
    def __init__(self, name, state, reactivity):
        self.name = name
        self.state = state  # e.g., solid, liquid, gas
        self.reactivity = reactivity  # e.g., low, medium, high

    def mix(self, other):
        if not isinstance(other, Chemical):
            raise ValueError("Can only mix with another Chemical")
        # Logic for mixing chemicals
        return f"Mixing {self.name} with {other.name}"

    def __str__(self):
        return f"{self.name} ({self.state}) - Reactivity: {self.reactivity}"