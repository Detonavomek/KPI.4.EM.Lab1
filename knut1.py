import math


class Digits():

    def __init__(self, value):
        self.digits = []
        self.positive = True
        value = float(value)

        if value < 0:
            self.positive = False
            value = 0.0 - value

        self.digits.insert(0, value % 10)
        value /= 10
        while value != 0:
            self.digits.insert(0, value % 10)
            value /= 10.0

    def get_value(self):
        result = 0
        for i in range(0, len(self.digits)):
            result *= 10.0
            result += self.digits[i]
        if not self.positive:
            result *= -1.0
        return result

    def next_max(self):
        return self.digits.pop()


class Knut():

    def __init__(self, seed):
        self.x = float(seed)

    def get_next(self):
        currentDigits = []
        digits = Digits(self.x)
        counter = digits.next_max()
        for i in range(0, int(counter)):
            step = digits.next_max() + 3
            if step <= 3:
                if self.x < 5000000000:
                    self.x += 5000000000
            if step <= 4:
                self.x = math.floor((self.x * self.x) / 100000.0) % 10000000000
            if step <= 5:
                self.x = (1001001001.0 * self.x) % 10000000000
            if step <= 6:
                if self.x < 100000000:
                    self.x += 9814055677
                else:
                    self.x = 10000000000 - self.x
            if step <= 7:
                first5 = self.x % 100000
                self.x = first5 * 100000 + (self.x / 100000.0)
            if step <= 8:
                self.x = (1001001001.0 * self.x) % 10000000000
            if step <= 9:
                currentDigits = Digits(self.x)
                for j in range(0, len(currentDigits.digits)):
                    if currentDigits.digits[j] != 0:
                        currentDigits.digits[j] -= currentDigits.digits[j]
            if step <= 10:
                if self.x < 100000:
                    self.x = self.x * self.x + 99999
                else:
                    self.x -= 99999
            if step <= 11:
                while self.x < 1000000000:
                    self.x *= 10.0
            if step <= 12:
                self.x = math.floor(
                    (self.x * (self.x - 1)) / 100000.0) % 10000000000
        return math.fabs(self.x)
