from random import randint
import time

class LCG:

    def __init__(self, a, c, mod):
        self.a = a
        self.c = c
        self.mod = mod

    def run(self, seed):
        number = (self.a * seed + self.c) % (2**self.mod)
        return number

class Fermat:

    def __init__(self):
        pass

    def mod(self, base, exponent, mod):
        x = 1
        y = base
        while exponent > 0:
            if exponent % 2 == 1:
                x = (x*y) % mod
            y = (y*y) % mod
            exponent = exponent / 2
        return x % mod


    def test(self, number, interactions):
        if number == 1:
            return False;
        for i in range(0, interactions):
            a = randint(0, number)
            if self.mod(a, number -1, number) != 1:
                return False
        return True

class MR:

    def __init__(self):
        pass

    def mod(self, base, exponent, mod):
        x = 1
        y = base
        while exponent > 0:
            if exponent % 2 == 1:
                x = (x*y) % mod
            y = (y*y) % mod
            exponent = exponent / 2
        return x % mod

    def mulmod(self, a, b, mod):
        x = 0
        y = a % mod
        while b > 0:
            if b % 2 == 1:
                x = (x + y) % mod
            y = (y * 2) % mod
            b /= 2;
        return x % mod

    def test(self, number, interactions):
        # Casos basicos
            # - se menor do que 2 (o primeiro inteiro primo) entao False
            # - se igual a 2 entao True
            # - se divisivel por 2 entao composto, logo False
        if number < 2:
            return False
        elif number == 2:
            return True
        elif number % 2 == 0:
            return False
        # Escrever (number - 1) como (2**s * d)
        s = number - 1
        while(s % 2 == 0):
            s /= 2
        for i in range(0, interactions):
            a = randint(0, number)
            temp = s;
            m = self.mod(a, temp, number)
            while(temp != number - 1 and m != 1 and m != number - 1):
                m = self.mulmod(m, m, number)
                temp *= 2
            if m != (number - 1) and temp % 2 == 0:
                return False

        return True

class XorShift():

    def __init__(self):
        pass

    def run(self, x, mod):
        x ^= x << 13
        x ^= x >> 17
        x ^= x << 5
        return x % (2**mod)

def prime():
    lcg = LCG(1664525, 1013904223, 16)
    fermat = Fermat()
    is_prime = False
    number = 127

    interactions = 50
    print(fermat.test(number, interactions))
    start_time = time.time()
    while(not is_prime):
        number = lcg.run(number) #8754
        is_prime = fermat.test(number, interactions)
    print("--- %s seconds ---" % (time.time() - start_time))
    print number

prime()

# def mr_prime():
#     interactions = 50
#     mr = MR()
#     start_time = time.time()
#     result = mr.test(23, interactions)
#     print("--- %s seconds ---" % (time.time() - start_time))
#     print result
#
# mr_prime()

# def xs_prime():
#     xs = XorShift()
#     mr = MR()
#     is_prime = False
#     number = 13
#     interactions = 50
#     start_time = time.time()
#     while(not is_prime):
#         number = xs.run(number, 4096)
#         is_prime = mr.test(number, interactions)
#     print("--- %s seconds ---" % (time.time() - start_time))
#     print number
#
# xs_prime()

# def mr_prime():
#     interactions = 50
#     fermat = Fermat()
#     start_time = time.time()
#     result = fermat.test(645193578781, interactions)
#     print("--- %s seconds ---" % (time.time() - start_time))
#     print result

# mr_prime()
