from random import randint
class MillerRabin:

    def __init__(self, iterations):
        self.iterations = iterations

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
            b = b / 2
        return x % mod

    def test_prime(self, random_number):
        if random_number < 2:
            return False
        if random_number != 2 and random_number % 2 == 0:
            return False
        s = random_number - 1
        while s % 2 == 0:
            s = s / 2
        for i in range(self.iterations):
            a = randint(0, random_number)
            temp = s
            mod = self.mod(a, temp, random_number)
            while temp != random_number - 1 and mod != 1 and mod != random_number - 1:
                mod = self.mulmod(mod, mod, random_number)
                temp = temp*2
            if mod != (random_number - 1) and temp % 2 == 0:
                return False

        return True
