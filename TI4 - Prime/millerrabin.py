from random import randint
import random
import time
class MillerRabin:

    def __init__(self, iterations):
        self.iterations = iterations

    #calculo da exponenciacao modular
    #base^exponent mod mod)
    def mod(self, base, exponent, mod):
        x = 1
        y = base
        while exponent > 0:
            if exponent % 2 == 1:
                x = (x*y) % mod
            y = (y*y) % mod
            exponent = int(exponent / 2)
        return x % mod

    #calcula (a * b) % c
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
        #se random_number for <2 ou diferente de 2 ou composto retorna False
        #se for = a 2 retorna True
        if random_number < 2:
            return False
        if random_number == 2:
            return True
        if random_number != 2 and random_number % 2 == 0:
            return False

        # random number n - 1 = 2^k * q
        #divide por 2 ate que impar, q = s
        s = random_number - 1
        while s % 2 == 0:
            s = s / 2
        for i in range(self.iterations):
            #gera numero a aleatorio menor que o random_number (inclusivo, exclusivo)
            a = randint(1, random_number)
            temp = s
            #a^q eh congruente a 1 modulo p??
            mod = self.mod(a, temp, random_number)

            while temp != random_number - 1 and mod != 1 and mod != random_number - 1:
                mod = self.mulmod(mod, mod, random_number)
                temp = temp*2
            if mod != (random_number - 1) and temp % 2 == 0:
                return False

        return True

BITS_NUMBER = (32, 40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096)
mr = MillerRabin(10)

for n_bits in BITS_NUMBER:
    random_number = 0
    is_prime = False
    sum_time = 0
    for i in range(10):
        time_before = int(round(time.time() * 1000000))
        while is_prime == False:
            random_number = random.getrandbits(n_bits)
            is_prime = mr.test_prime(random_number)

        time_after = int(round(time.time() * 1000000))
        sum_time += time_after - time_before

    print("Tempo Miller-Rabin " + str(n_bits) + "bits : ", sum_time/10, " microsegundos")
    print("Prime Miller-Rabin " + str(n_bits) + "bits : ", random_number)
