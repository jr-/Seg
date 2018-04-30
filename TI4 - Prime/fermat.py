from random import randint
class Fermat:

    def __init__(self, iterations):
        self.iterations = iterations

    def modulo(self, base, exponent, mod):
        x = 1
        y = base
        while exponent > 0:
            if exponent % 2 == 1:
                x = (x * y) % mod
            y = (y * y) % mod
            exponent = exponent / 2
        return x % mod


    def test_prime(self, random_number):
        if random_number == 1:
            return False;
        for i in range(0, 10):
            a = randint(0, random_number)
            if self.modulo(a, random_number - 1, random_number) != 1:
                return False
        return True
