import math

from knut1 import Digits
from cts5 import CTS


class Mine():

    def __init__(self):
        self.a1 = 2.5
        self.a2 = 6.0
        self.n = -1.0
        self.x = {
            -2: 3,
            -1: 17
        }
        self.p = math.pow(4, 12) - 1

    def get_next(self):
        self.n = self.n + 1
        if self.n % 2:
            self.x[self.n] = (
                self.a2 * self.x.get(self.n - 1) + self.a1 * self.x.get(self.n - 2)) % self.p
        else:
            self.x[self.n] = (
                self.x.get(self.n - 1) + self.x.get(self.n - 2)) % self.p
        return self.x.get(self.n)
