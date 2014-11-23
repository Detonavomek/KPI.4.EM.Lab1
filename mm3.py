import math
from period import Period
from lkm2 import LKM


class MM():

    def __init__(self, m, count):
        self.m = m
        self.k = 128
        self.N = count
        self.V = []
        self.Z = []
        self.V = LKM(7, 5, 3, self.m).get_arr(self.N)
        self.x = LKM(5, 7, 3, self.m).get_arr(self.N)
        self.y = LKM(5, 7, 9, self.m).get_arr(self.N)
        for i in range(0, self.N):
            self.res = self.V[self.y[i]]
            self.V[self.y[i]] = self.x[i]
            self.Z.append(self.res)

    def get_next(self):
        try:
            return self.Z.pop()
        except:
            return 0
