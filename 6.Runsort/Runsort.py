import sys

def isSorted(array):
    for i in range(0,len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True   
    
# from Sedgewick and Wayne, Section 2.2    
def merge(array, aux, lo1, hi1, lo2, hi2):
    # copy to aux[]
    for k in range(lo1, hi1+1):
            aux[k] = array[k]
            
    # merge back to a[]
    low1 , low2 = lo1, lo2
    for k in range(low1, hi2+1):
        if low1 > hi1:
            array[k] = array[low2]
            low2 += 1
        elif low2 > hi2:
            array[k] = aux[low1]
            low1 += 1
        elif aux[low1] <= array[low2]:
            array[k] = aux[low1]
            low1 += 1
        else:
            array[k] = array[low2]
            low2 += 1
                
def runsort(array):
    k=0;
    while not isSorted(array):
        run1_lo = 0
        #print(len(array))
        aux = [None] * len(array)  
        
        while run1_lo < len(array) :    
            run1_hi = run1_lo           
        
            while run1_hi < len(array) - 1 and array[run1_hi +1] >= array [run1_hi]:
                run1_hi +=1
            
            print("Run1 from lo: ", run1_lo, " to hi: ", run1_hi)    
        
            run2_lo = run1_hi + 1
            run2_hi = run2_lo
            
            if run2_hi >= len(array): break
            
            while run2_hi+1 < len(array) and array[run2_hi+1] >= array[run2_hi]:
                run2_hi += 1
                 
            print("Run2 from lo: ", run2_lo, " to hi: ", run2_hi)     
            
                    
            print("Merged from id: ", run1_lo, "<->", run1_hi, " and ", run2_lo, "<->", run2_lo, " =>", end= " ")
            merge(array, aux, run1_lo, run1_hi, run2_lo, run2_hi)
            for i in range (0, len(array)):
                print(array[i], end=" ")
            
            print()
            
            run1_lo = run2_hi + 1
        
        
        #merge(array, aux, run1_lo, run1_hi, run2_lo, run2_hi)
          
        for i in range (0, len(array)):
            print(array[i], end=" ")
        print();print();
        
        k+=1
        
        if (k == 6): 
            break
        
def findReversedRuns(array):
    run1_lo = 0
    while run1_lo < len(array) :    
            run1_hi = run1_lo           
        
            while run1_hi < len(array) - 1 and array[run1_hi +1] <= array [run1_hi]:
                run1_hi +=1
            
            
            if not run1_lo == run1_hi:
                print("Reversed run from lo: ", run1_lo, " to hi: ", run1_hi, ": " , end= " ")    
                for i in range (run1_lo, run1_hi+1):
                    print(array[i], end=" ")
                print()
                
                for i in range(0, (run1_hi-run1_lo)):
                    array[run1_lo+i], array[run1_hi-i] = array[run1_hi-i] , array[run1_lo+i]
                   # print("swapping", array[run1_lo + i]," with ", array[run1_hi-i])
                
            run1_lo = run1_hi + 1

if len(sys.argv) > 1:
        try:
            sys.stdin = open(sys.argv[1])
        except IOError:
            print("File not found, using standard input instead")    

Phrase = []
Input = sys.stdin.readline()

for i in range (0, len(Input)):
    if not Input[i].isspace():
        Phrase.append(Input[i])

'''
for i in range (0, len(Phrase)):
    print(Phrase[i], end=" ")
print()
'''

findReversedRuns(Phrase)

print()
for i in range (0, len(Phrase)):
                print(Phrase[i], end=" ")
            
print()

runsort(Phrase)





