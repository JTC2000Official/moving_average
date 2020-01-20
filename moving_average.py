"""

"""

class MovingAverage():
    def __init__(self, N):
        self.N = N
        self.samples = (11,22,23,13,5)

    def addSample(self, value):
        self.samples.append(value)
        if self.samples == self.N
    def getAverage(self):
        if len(self.samples) < self.N:
            return sum(self.samples)/len(self.samples)
        else:
            return sum(self.samples)/self.N

if __name__ == "__main__":
    a = MovingAverage(10)
    a.getAverage()
