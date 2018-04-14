from lcg import LCG
from xorshift import XorShift
from bbs import BBS
import time
import random

BITS_NUMBER = (32, 40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096)
#calcula uma media de tempo de execução para cada tamanho de número de BITS_NUMBER
def test_time_bbs():
        for n_bits in BITS_NUMBER:
            #print de um numero aleatorio gerado
            bbs = BBS(n_bits)
            print("BBS " + str(n_bits) + "bits : ", bbs.generate_random())

            #gera 100 numeros aleatorios com o bbs e pega a media do tempo
            sum_time = 0
            for i in range(100):
                time_before = int(round(time.time() * 1000000))
                bbs = BBS(n_bits)
                bbs.generate_random()
                time_after = int(round(time.time() * 1000000))
                sum_time += time_after - time_before
            print("tempo BBS " + str(n_bits) + "bits :", sum_time/100, " microsegundos")
#calcula uma media de tempo de execução para cada tamanho de número de BITS_NUMBER
def test_time_lcg():
        for n_bits in BITS_NUMBER:
            lcg = LCG(1664525, 1013904223, 2**n_bits, random.getrandbits(n_bits))
            #print de um numero aleatorio gerado
            print("LCG " + str(n_bits) + "bits : ", lcg.generate_random())

            #gera 100 numeros aleatorios com o lcg e pega a media do tempo
            sum_time = 0
            for i in range(100):
                time_before = int(round(time.time() * 1000000))
                lcg.generate_random()
                time_after = int(round(time.time() * 1000000))
                sum_time += time_after - time_before
            print("tempo LCG " + str(n_bits) + "bits :", sum_time/100, " microsegundos")
#calcula uma media de tempo de execução para números de 32bits
def test_time_xs():
    #32bit XorShift
    xs = XorShift(2**32, random.getrandbits(32))
    #print de um numero aleatorio gerado
    print("XorShift 32bits : ", xs.generate_random())

    #gera 100 numeros aleatorios com o XorShift e pega a media do tempo
    sum_time = 0
    for i in range(100):
        time_before = int(round(time.time() * 1000000))
        xs_rn1 = xs.generate_random()
        time_after = int(round(time.time() * 1000000))
        sum_time += time_after - time_before
    print("tempo XS 32bits : ", sum_time/100, " microsegundos")


if __name__ == '__main__':
    test_time_bbs()
    test_time_lcg()
    test_time_xs()
