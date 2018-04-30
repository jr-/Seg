from random import randint
import random
import time
class Fermat:

    def __init__(self, iterations):
        self.iterations = iterations

    #calculo da exponenciacao modular
    #calcula esse lado a^p-1(mod p) ///congruente 1(mod p)
    #a = base, p-1 = exponent, mod p = mod
    def modulo(self, base, exponent, mod):
        x = 1
        y = base
        while exponent > 0:
            if exponent % 2 == 1:
                x = (x * y) % mod
            y = (y * y) % mod
            exponent = int(exponent / 2)
        return x % mod

    #testa se o random_number eh primo com a quantidade de iteracoes/testes = iterations
    def test_prime(self, random_number):
        if random_number == 1:
            return False;
        for i in range(0, self.iterations):
            #gera numero a aleatorio menor que o random_number (inclusivo, exclusivo)
            a = randint(1, random_number)
            #eh congruente funcao modulo eh congruente a 1(mod p)
            if self.modulo(a, random_number - 1, random_number) != 1:
                return False
        return True

BITS_NUMBER = (32, 40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096)
fermat = Fermat(10)

for n_bits in BITS_NUMBER:
    random_number = 0
    is_prime = False
    sum_time = 0
    for i in range(10):
        time_before = int(round(time.time() * 1000000))
        while is_prime == False:
            random_number = random.getrandbits(n_bits)
            is_prime = fermat.test_prime(random_number)

        time_after = int(round(time.time() * 1000000))
        sum_time += time_after - time_before

    print("Tempo Fermat " + str(n_bits) + "bits : ", sum_time/10, " microsegundos")
    print("Prime Fermat " + str(n_bits) + "bits : ", random_number)
