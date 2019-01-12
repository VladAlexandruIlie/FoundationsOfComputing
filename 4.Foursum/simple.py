from __future__ import print_function
import time
import sys

N = int(sys.stdin.readline())
vals = list(map(int, sys.stdin.readlines()))

start_time = time.time()
for i in range(0, N):
    for j in range(i+1,N):
        for k in range(j+1, N):
            for l in range(k+1, N):
                if vals[i]+vals[j]+vals[k]+vals[l] == 0:
                    #print(i,j,k,l,file=sys.stderr)
                    #print(vals[i],vals[j],vals[k],vals[l],file=sys.stderr)
                    #print("--- %.6s seconds ---" % (time.time() - start_time))
                    print(True)
                    sys.exit()
                    
#print("--- %.6s seconds ---" % (time.time() - start_time))
print(False)
