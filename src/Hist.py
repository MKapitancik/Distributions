from src._DictContainer import _DictContainer

class Hist(_DictContainer):
    def __init__(self, l: list):
        _DictContainer.__init__(self)
        
        for x in l:
            self.increment(x)        

    def freq(self, val) -> int:
        return self.__getitem__(val)

    def x_y(self) -> [list, list]:
        x = list(sorted(self.d))
        y = [self[xi] for xi in x]

        return x, y

