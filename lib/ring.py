class Ring:
    def __init__(self, values=None):
        if values is None:
            values = [0, 0, 0, 0, 0]
        self.values = values

    def rotate(self, n=1, reverse=False):
        n = n % len(self.values)
        if reverse:
            self.values = self.values[n:] + self.values[:n]
        else:
            self.values = self.values[-n:] + self.values[:-n]
