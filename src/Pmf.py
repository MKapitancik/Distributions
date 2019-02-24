from src._DictContainer import _DictContainer

class Pmf(_DictContainer):
    def __init__(self, l: list):
        _DictContainer.__init__(self)
        
        for x in l:
            self.increment(x)        
    
    def normalize(self, fraction=1.0):
        total = self.total()
        if(total is 0.0):
            raise ValueError('There is values')        
        factor = float(fraction) / total

        for i in self.d.keys():
            self.d[i] *= factor

    def x_y(self) -> [list, list]:
        x = list(sorted(self.d))
        y = [self[xi] for xi in x]

        return x, y