from period import Period


class CTS():

    @staticmethod
    def fibo(a, b, m, n):
        A = []
        A.append(a % m)
        A.append(b % m)
        for i in range(2, n):
            A.append((A[-1] + A[-2]) % m)
        return A

    def __init__(self, mx, my):
        self.X = CTS.fibo(4589, 8459, mx, mx)
        self.Y = CTS.fibo(215, 4856, mx, my)
        self.Z = []
        for i in range(0, my):
            self.Z.append((self.X[i] - self.Y[i]) % mx)

    def get_next(self):
        try:
            return self.Z.pop()
        except:
            return 0
