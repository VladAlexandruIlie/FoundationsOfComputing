from algs4.fundamentals.java_helper import java_string_hash, trailing_zeros
from algs4.stdlib import stdio
import math
import time
import sys

class KGrams:
    def __init__(self, key, k):
        self.kGrams = []
        self.key = key
        self.k = k+1
        for i in range(0,self.k):
            igram = []
            self.kGrams.append(igram)
        self.createAll()
    
    def createAll(self):
        for i in range(1,self.k):
            self.createLayer(i)
    
    def createLayer(self, length):
        for i in range(0,len(self.key)-length+1):
            substring = self.key[i:i+length]
            self.kGrams[length].append(substring)
            #print(substring)

    def getKGrams(self):
        return self.kGrams

def createProfile(sequence, k, d):
    profile = [0] * (d+1)
    kgram = KGrams(sequence,d)
    for l in kgram.getKGrams():
        for i in range(0,len(l)):
            code = java_string_hash(l[i]) % d
            profile[code] += 1      
    return profile

def EuclidLen(p):
    length = 0
    for i in range(0, len(p)):
        length = length + p[i]*p[i]
    return math.sqrt(length)
        
def similarity(p, q):
    if (len(p) != len(q)): return
    dotProduct = 0
    for i in range(0, len(p)):
        dotProduct = dotProduct + p[i]*q[i]
    
    len_p = EuclidLen(p)
    len_q = EuclidLen(q)
    length = len_p * len_q
    
    #print(dotProduct, length)
    
    return dotProduct/length

start_time = time.time()
    
if len(sys.argv) > 1:
    try:
       sys.stdin = open(sys.argv[1])
    except IOError:
        print("File not found")  

K = 20
D = 10000
keys = []
sequences = []

# reading the data
sequence = ""; finalSequence=""
while not stdio.isEmpty():
    line = stdio.readLine()
    if (line.startswith('>')):
        firstLine = line.split(" ")
        name = firstLine[0][1:]
        keys.append(name)
        sequence = ""
        finalSequence = ""
    else:
        sequence = sequence + line
        if (len(sequence) > 2 ): finalSequence = sequence
    if (finalSequence!=""):
        sequences.append(finalSequence)
        
# checking if the file was read correctly 
for i in range(0,len(keys)):
    print(keys[i]," >",sequences[i], " length: " , len(sequences[i]))
print()
profiles = []

# create species profiles
for i in range(0,len(keys)):
    prof = createProfile(sequences[i], K, D)
    profiles.append(prof)

# check profile creation and similarity

for i in range(0,len(keys)):
    print(keys[i], " > ", profiles[i])
print()

print("Printing simmilarity table between species; K = ", K, " and D = ", D)
for i in range(0,len(keys)):
    print ("%15s" % keys[i], end=" & ")
    
    for j in range(0, len(keys)):
        #print("%5s %.5f " % (keys[j], similarity(profiles[i], profiles[j])), end =" ")
        print("%.4f &" % (similarity(profiles[i], profiles[j])), end =" ")
    print()
print()
testProfiles = [[0,1,1],[0,0,2]]

for i in range(0,len(testProfiles)):
    print ("%15s" % testProfiles[i], end=" & ")
    
    for j in range(0, len(testProfiles)):
        #print("%5s %.5f " % (keys[j], similarity(profiles[i], profiles[j])), end =" ")
        print("%.4f &" % (similarity(testProfiles[i], testProfiles[j])), end =" ")
    print() 
    
print("Exercution time: --- %s seconds ---" % (time.time() - start_time))
