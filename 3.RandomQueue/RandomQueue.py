from algs4.stdlib.stdrandom import uniform,shuffle
from algs4.stdlib.stdstats import mean,stddev
#from algs4.stdlib.stdio import eprint
import sys
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


class RandomQueue:
    def __init__(self):
        self._randomQueue = [] #iniciuojam array

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def size(self):
        return len(self._randomQueue)

    #def __len__(self):
    #    self._counter = 1
    #    if self._randomQueue.hasNext:
    #        counter += 1
    #    return self._counter

    def enqueue(self,item):
        self._randomQueue.append(item)

    def sample(self):
        hi = self.size()
        index = uniform(hi)
        try:
            self._randomItem = self._randomQueue[index]
        except RuntimError:
            raise
        return self._randomItem

    def dequeue(self):
        hi = self.size()
        index = uniform(hi)
        try:
            randomItem = self._randomQueue[index]
            del self._randomQueue[index]
        except RuntimeError:
            raise
        return randomItem

    def __iter__(self):
        """
        Returns an iterator that iterates over the items in this RandomQueue in random order.
        :returns: an iterator that iterates over the items in this RandomQueue in random order.
        """
        shuffle(self._randomQueue)
        for N in self._randomQueue:
            yield N