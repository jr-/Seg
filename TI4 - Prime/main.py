from bbs import BBS
from fermat import Fermat
from millerrabin import MillerRabin
import time
import random

BITS_NUMBER = (32, 40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096)
#calcula uma media de tempo de execução para geração de números primos aleatórios de tamanho BITS_NUMBER
#utilizando o teste de primalidade MillerRabin
# def test_time_miller_rabin():
#     pass

#calcula uma media de tempo de execução para geração de números primos aleatórios de tamanho BITS_NUMBER
#utilizando o teste de primalidade Fermat
# def test_time_fermat():
#     pass

if __name__ == '__main__':
    fermat = Fermat(10)
    random_number = 0
    is_prime = False

    while is_prime == False:
        random_number = 127
        is_prime = fermat.test_prime(random_number)
        print(is_prime)


    print(random_number)
