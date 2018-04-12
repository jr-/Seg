class LCG:
    def __init__(self, a, c, m, seed):
        self.a = a
        self.c = c
        self.m = m
        self.seed = (self.a * seed) % (self.m)

    def generate_random(self):
        self.seed = (self.a * self.seed + self.c) % (self.m)
        return self.seed
