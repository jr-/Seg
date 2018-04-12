from lcg import LCG
from xorshift import XorShift
from mwc import MWC
from bbs import BBS
import time
import random

if __name__ == '__main__':
    lcg = LCG(1664525, 1013904223, 2**32, int(time.clock()))
    lcg_rn1 = lcg.generate_random()
    print("LCG:", lcg_rn1)
    print("Tamanho:", lcg_rn1.bit_length())

    #32bit XorShift
    xs = XorShift()
    xs_rn1 = xs.generate_random(random.getrandbits(4096), 2**32)
    print("XS:", xs_rn1)
    print("Tamanho:", xs_rn1.bit_length())

    #TODO Bib para pegar 2 números coprimos, para gerar o N
    bbs = BBS(192649, 101355)
    bbs_rn1 = bbs.generate_random()
    print("BBS:", bbs_rn1)
    print("Tamanho:", bbs_rn1)


    #print("Random:", random.getrandbits(4096))
