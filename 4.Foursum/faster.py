from __future__ import print_function
import time
import sys


def binarySearch(array, value):
    lo = 0
    hi = len(array) - 1
    while hi >= lo:
        mid = lo + (hi - lo)//2
        if array[mid] > value:
            hi = mid - 1
        elif array[mid] < value:
            lo = mid + 1 
        else: 
            return mid
    return -1

N = int(sys.stdin.readline())
vals = list(map(int, sys.stdin.readlines()))

start_time = time.time()

for i in range(0, N):
    for j in range(i+1,N):
        if vals[i] > vals[j]:
            vals[i], vals[j] = vals[j], vals[i]

pre_search_processing = time.time() - start_time

for i in range(0, N):
    for j in range(i+1,N):
        for k in range(j+1, N):
                if (binarySearch(vals, -(vals[i]+vals[j]+vals[k])) ) > k:
                    #print(i,j,k,binarySearch(vals, -(vals[i]+vals[j]+vals[k])),file=sys.stderr)
                    #print(vals[i],vals[j],vals[k],vals[l],file=sys.stderr)
                    print("--- %.6s seconds ---" % (time.time() - start_time))
                    print(True)
                    sys.exit()

print("--- %.4s seconds ---" % (time.time() - start_time))
print(False)
