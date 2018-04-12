class XorShift():
    def __init__(self):
        pass

    def generate_random(self, x, m):
        x ^= x << 13
        x ^= x >> 17
        x ^= x << 5
        return x % (m)
