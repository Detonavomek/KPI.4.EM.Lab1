from period import Period


class LKM():

    def __init__(self, x, a, c, m):
        self.x = x
        self.a = a
        self.c = c
        self.m = m

    def get_next(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def get_arr(self, count):
        self.arr = []
        for i in range(0, count):
            self.x = (self.a * self.x + self.c) % self.m
            self.arr.append(self.x)
        return self.arr
