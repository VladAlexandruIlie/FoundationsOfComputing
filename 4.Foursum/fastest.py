from __future__ import print_function
from algs4.sorting import quicksort
from algs4.stdlib import stdrandom, stdio
import time
import sys

class pairSum:
    def __init__(self,sum,firstIndex, secondIndex):
        self.sum = sum
        self.firstIndex = firstIndex
        self.secondIndex  = secondIndex
  
    def _sum(self):
       return self.sum
    def _firstIndex(self):
        return self.firstIndex
    def _secondIndex(self):
        return self.secondIndex
        
def binarySearch(array, value):
    lo = 0
    hi = len(array) - 1
    while hi >= lo:
        mid = lo + (hi - lo)//2
        if array[mid]._sum() > value:
            hi = mid - 1
        elif array[mid]._sum() < value:
            lo = mid + 1 
        else: 
            return mid
    return -1
    
def sort(array):
    """
    Rearranges the array in ascending order, using the natural order
    """
    
    _sort(array, 0, len(array) - 1)

# quicksort the subarray from array[lo] to array[hi]
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

        while array[i+1]._sum() < v._sum():
            i += 1
            if i == hi:
                break
        i += 1

        # find item on hi to swap
        while v._sum() < array[j-1]._sum():
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
    


N = int(sys.stdin.readline())
vals = list(map(int, sys.stdin.readlines()))
quicksort.sort(vals)

'''
for i in range (0,N):
    print(vals[i], end =" ")
print("")
for i in range (0,N):
    print(i, end =" ")
print("")
print("")
'''

start_time2 = time.time()

N2 = int((N*(N -1))/2)
pairs = [] * N2

for i in range (0,N-1):
    for j in range (i+1,N):
            pairs.append(pairSum( vals[i] + vals[j], i, j))
    
#N2 = len(pairs)
    
'''
for i in range (0,N2):
    print(pairs[i]._sum(), end =" ")
print("")

for i in range (0,N2):
    print(pairs[i]._firstIndex(), end =" ")
print("")

for i in range (0,N2):
    print(pairs[i]._secondIndex(), end =" ")
print("")
'''
    
sort(pairs)
#print("")

    
#print("--- %.6s seconds --- ; sorting using quicksort " % (time.time() - start_time2))

start_time = time.time()

for i in range(0, N2):
    pos2 = binarySearch(pairs, -(pairs[i]._sum()))
    if pos2 > 0 and pairs[i]._firstIndex() != pairs[pos2]._firstIndex() and pairs[i]._secondIndex() != pairs[pos2]._secondIndex() and pairs[i]._secondIndex() != pairs[pos2]._firstIndex() and pairs[i]._firstIndex() != pairs[pos2]._secondIndex():
        #print("--- %.6s seconds --- ; searching for pairs" % (time.time() - start_time))
        #print("--- %.6s seconds --- ; Total running time " % (time.time() - start_time2))
        print(True)
        sys.exit()
        
#print("--- %.6s seconds --- ; searching for pairs " % (time.time() - start_time))
#print("--- %.6s seconds --- ; Total running time " % (time.time() - start_time2))
print(False)
