class MovingAverage():
    def __init__(self, N):
        self.N = N
        self.samples = []

    def addSample(self, value):
        self.samples.append(value)
        if len(self.samples) > self.N:
            self.samples.pop(0)
        return self.samples

    def getAverage(self):
        if len(self.samples) < self.N:
            return sum(self.samples)/len(self.samples)
        else:
            return sum(self.samples)/self.N
