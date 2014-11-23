import math
from period import Period


class PM():

    def __init__(self):
        self.a1 = 2  # a^1
        self.a2 = 4  # a^2
        self.n = -1
        self.x = {
            -2: 3,
            -1: 17
        }
        self.p = math.pow(2, 32) - 1

    def get_next(self):
        self.n = self.n + 1
        self.x[self.n] = (
            self.a1 * self.x.get(self.n - 1) + self.a2 * self.x.get(self.n - 2)) % self.p
        return self.x.get(self.n)
