import sys
import time
from MyUnionFind2 import MyUnionFind
from algs4.stdlib import stdio
 
if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            sys.stdin = open(sys.argv[1])
        except IOError:
            print("File not found, using standard input instead")
    start_time = time.time()
    n = stdio.readInt()
    qf = MyUnionFind(n)
     
    step = 0
    connectedStep = 0
    giantComponentStep = 0
    isolatedStep = 0
    connected = 0
         
    while not stdio.isEmpty() and connected == 0:
        #for i in range(n): print(qf._id[i], end=" ") print("")
        step += 1
        p = stdio.readInt()
        q = stdio.readInt()
        if qf.connected(p, q):
            continue
        qf.union(p, q)  
             
        if qf.count()== 1 and connected == 0:
            connectedStep = step 
            connected = 1
                 
        max = qf._biggestComponent
        if max > round(n/2) and giantComponentStep == 0:
            giantComponentStep = step
             
        isolated = qf._isolates
        if isolated == 0 and isolatedStep == 0:
            isolatedStep = step
               
    print(n, isolatedStep , giantComponentStep, connectedStep)      
    #print("--- %s seconds ---" % (time.time() - start_time))