class BBS:
    def __init__(self, mod, seed):
        self.mod = mod
        self.seed = seed
        pass

    def generate_random(self):
        self.seed = (self.seed**2) % self.mod
        return self.seed
