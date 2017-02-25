#!/usr/bin/env python3
import time

class Random(object):
    """
    Simplified Java SE 6 random number generator.
    Adapted from https://github.com/MostAwesomeDude/java-random
    """

    def __init__(self, seed = None):
        if seed is None:
            seed = int(time.time() * 1000)
        self.seed = seed

    @property
    def seed(self):
        return self._seed

    @seed.setter
    def seed(self, seed):
        self._seed = (seed ^ 0x5deece66d) & ((1 << 48) -1)

    def next(self, bits):
        """
        Generate next random number.
        Method returns an int that is `bits` bits long.
        Each bit is nearly equally likely to be 0 or 1.
        """

        if bits < 1:
            bits = 1
        elif bits > 32:
            bits = 32

        self._seed = (self._seed * 0x5deece66d + 0xb) & ((1 << 48) -1)
        retval = self._seed >> (48 - bits)

        if retval & (1 << 31):
            retval -= (1 << 32)

        return retval

    def nextInt(self, n = None):
        """
        Return random int in [0, `n`).
        If `n` is not supplied, random 32-bit int will be returned
        """
        if n is None:
            return self.next(32)

        if n <= 0:
            raise valueError("Argument must be positive!")

        if not (n & (n-1)):
            return (n * self.next(31)) >> 31

        bits = self.next(31)
        val = bits % n
        while (bits - val + n - 1) < 0:
            bits = self.next(31)
            val = bits % n

        return val


n = int(input())
for _ in range(n):
    numbers = list(map(int,input().split()))
    r = Random(42);

    print (numbers)

