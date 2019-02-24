from abc import ABC

class _DictContainer(ABC):
    def __init__(self):
        self.d = {}            

    def __getitem__(self, x):
        if (x in self.d):
            return self.d[x]
        else:
            return 0

    def increment(self, x, term = 1):
        self.d[x] = self.d.get(x, 0) + term

    def remove(self, x):
        del self.d[x]
    
    def multiply(self, x, factor):
        self.d[x] = self.d.get(x) * factor
    
    def total(self):
        total = 0.0
        for i in self.d.values():
            total += i
        return total