class XorShift():
    def __init__(self, mod, seed):
        self.seed = seed
        self.mod = mod
        pass

    def generate_random(self):
        x = self.seed
        x ^= x << 13
        x ^= x >> 17
        x ^= x << 5
        self.seed = x % self.mod
        return self.seed
