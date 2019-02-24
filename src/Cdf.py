from src._DictContainer import _DictContainer
from src.Hist import Hist
from itertools import accumulate

class Cdf(_DictContainer):
    def __init__(self, l: list):
        _DictContainer.__init__(self)
        hist = Hist(l)

        self.xs, freq = zip(*hist.d.items())
        self.xp = list(map(float, accumulate(freq)))
        self.xp = [ x / self.xp[-1] for x in self.xp]
        self.xs = [0] + list(self.xs)
        self.xp = [0.0] + list(self.xp)

    def x(self):
        return list(map(str, self.xs))

    def y(self):
        return self.xp