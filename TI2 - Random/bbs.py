import random
import gmpy
from fractions import gcd

class BBS:
    #inicializa com a grandeza/numero de bits que deseja gerar os numeros aleatorios
    #: a pseudorandom bit sequence z1, z2,... ,zl of length l is generated.
    def __init__(self, n_bits):
        self.n_bits = n_bits
        self.mod = 0
        self.seed = 0
        self.p = 0
        self.q = 0

    def get_p(self):
        return self.p

    def get_q(self):
        return self.q

    def get_mod(self):
        return self.mod

    def get_seed(self):
        return self.seed

    # Gera os numeros primos p e q e retorna o valor de n = mod
    #p x q = n = mod
    # p = q = 3 (mod 4)
    #nem sempre essa funcao faz o mod ter o n_bits desejado
    #1. Setup. Generate two large secret random (and distinct) primes p and q (cf. Note 8.8), each congruent to 3 modulo 4, and compute n = pq.
    def generate_mod(self):
        n_bits_primes = int(self.n_bits/2)
        while self.p == 0:
            #gera um numero aleatorio com uma grandeza de n_bits/2 e pega o proximo numero primo provavel
            p = gmpy.next_prime(random.getrandbits(n_bits_primes))
            if p % 4 == 3:
                self.p = p
        while self.q == 0 or self.q == self.p:
            q = gmpy.next_prime(random.getrandbits(n_bits_primes))
            if q % 4 == 3:
                self.q = q
        self.mod = self.p * self.q
        return self.mod

    #gera o valor da semente, a semente eh um numero aleatorio que seja relativamente primo de n = mod e retorna o valor da semente
    #nem p nem q podem ser fatores de seed
    #2. Select a random integer s (the seed) in the interval [1, n−1]such that gcd(s, n)=1, and compute x0←s2 mod n
    def generate_seed(self):
        while self.seed == 0:
            seed = random.getrandbits(self.mod.bit_length())
            if gcd(seed, self.mod) == 1 and self.seed < self.mod:
                self.seed = seed
        return self.seed

    #For i from 1 to l do the following:
    # 3.1 xi←x2i−1 mod n=mod.
    # 3.2 zi← the least significant bit of xi.
    def generate_random(self):
        self.generate_mod()
        self.generate_seed()
        self.seed = (self.seed**2) % self.mod
        z = 0
        if self.seed != 0 and self.mod != 0:
            for i in range(self.n_bits):
                self.seed = (self.seed**2) % self.mod
                z = (z << 1) | self.seed % 2
            return z
        return 0
