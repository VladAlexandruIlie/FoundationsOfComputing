import sys
import math
import time
import bisect
from algs4.stdlib import stdio

class State:
    def __init__(self, name, population):
        self.name = name.rstrip()
        self.population = int(population)
        self.currentSeats = 1
        self.priority = self.population / (math.sqrt( self.currentSeats * (self.currentSeats + 1)) )
    
    def __lt__(self, other):
        return self.priority > other.priority
        
    def _name(self):
        return self.name
    
    def increaseSeats(self):
        self.priority = math.sqrt(self.currentSeats/ (self.currentSeats+2)) * self.priority
        self.currentSeats +=1
        
    def _population(self):
        return self.population
        
    def _priority(self):
        return self.priority


def printstates(array):
    for i in range (0, numberOfStates):
        #print ("{0:s}, {1:d}: {2:d} -> {3:.3f} ".format( array[i].name, array[i].population, array[i].currentSeats, array[i].priority) )
        #print ("{0:s} {1:d}".format( array[i].name, array[i].currentSeats))
        print (array[i].name, array[i].currentSeats)

#quicksort for initial array
'''
def sort(array):
    _sort(array, 0, len(array) - 1)

# quicksort
def _sort(array, lo, hi):
    if hi <= lo:
        return
    j = _partition(array, lo, hi)
    _sort(array, lo, j-1)
    _sort(array, j+1, hi)

# partition the subarray array[lo..hi] so that
# array[lo..j-1] <= array[j] <= array[j+1..hi]
# and return the index j
def _partition(array, lo, hi):
    i = lo
    j = hi + 1
    v = array[lo]
    while True:

        while v.priority < array[i+1].priority:
            i += 1
            if i == hi:
                break
        i += 1

        # find item on hi to swap
        while v._priority() > array[j-1]._priority():
            j -= 1
            if j == lo:
                break
        j -= 1

        # check if pointers cross
        if i >= j:
            break

        _exch(array, i, j)

    # put partitioning item v at a[j]
    _exch(array, lo, j)

    # now array[lo .. j-1] <= a[j] <= a[j+1 .. hi]
    return j

def _exch(array, i, j):
    array[i] , array[j] = array[j] , array[i]
'''         
#insertionsort for semi-sorted list of states
'''
def insertionSort(array):
    for i in range (1, len(array)):
        j = i
        while j>0 and array[j-1].priority < array[j].priority:
            array[j-1], array[j] = array[j] , array[j-1]
            j -= 1
        #array[j] , array[i] = array[i], array[j]
'''

         
if len(sys.argv) > 1:
        try:
            sys.stdin = open(sys.argv[1])
        except IOError:
            print("File not found, using standard input instead")    

startTime = time.time()
States = []

numberOfStates = int(sys.stdin.readline())
numberOfSeats = int(sys.stdin.readline())
#print ("number Of States: ", numberOfStates, ", number Of Seats: ", numberOfSeats )      

while not stdio.isEmpty():   
    name = stdio.readLine()
    population = stdio.readLine()
    States.append(State(name,population))

statesCopy = sorted(list(States))

    
remainingSeats = numberOfSeats - numberOfStates

while remainingSeats > 0:
    statesCopy[0].increaseSeats()
    remainingSeats -= 1
    
    toInsert = statesCopy[0]
    del statesCopy[0]
    
    bisect.insort(statesCopy, toInsert)
    
    #_exch(statesCopy, 0, len(statesCopy) -1
    #insertionSort(statesCopy)
    #sort(statesCopy)
    
    #printstates(statesCopy)
    #print("===========")
   


printstates(States)
#print("--- %.6s seconds ---" % (time.time() - startTime))