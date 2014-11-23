class Period():

    def __init__(self, obj, accuracy=10000):
        self.obj = obj
        self.accuracy = accuracy

    def find_period(self):
        numbers = []
        while True:
            hash = self.obj.get_next()
            try:
                index = numbers.index(hash)
                stopped = len(numbers)
                return stopped
            except:
                numbers.append(hash)
            if len(numbers) > self.accuracy:
                return self.accuracy
