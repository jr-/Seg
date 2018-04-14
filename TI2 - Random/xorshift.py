class XorShift():
    #seta os valores do algoritmo xorshift32bits
    #mod = modulo e seed = semente
    def __init__(self, mod, seed):
        self.seed = seed
        self.mod = mod
        pass
    #algoritmo xorshift32 bits do artigo Xorshift RNGs de George Marsaglia
    def generate_random(self):
        x = self.seed
        x ^= x << 13
        x ^= x >> 17
        x ^= x << 5
        self.seed = x % self.mod
        return self.seed
