class LCG:
    #seta os valores do algoritmo congruencia linear
    #m = modulo; a = multiplicador; c = incremento; seed = x0
    def __init__(self, a, c, m, seed):
        self.a = a
        self.c = c
        self.m = m
        self.seed = seed

    #gera o numero aleatorio Xi = (a*xi-1 + c) % modulo
    def generate_random(self):
        self.seed = (self.a * self.seed + self.c) % (self.m)
        return self.seed
