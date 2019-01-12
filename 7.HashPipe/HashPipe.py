from algs4.fundamentals.java_helper import java_string_hash, trailing_zeros
import sys

class Node:
    def __init__(self):
        self.key = None
        self.value = None
        self.next = None
    def _value(self):
        return self.value    
    def _key(self):
        return self.key
    def _next(self):
        return self.next
    def __repr__(self):
        return "|%s:%s|" % (self.key, self.value)

class HashPipe:
    def __init__(self):
        self.roots = []
         
        for i in range(0,33):
            first = Node()
            self.roots.append(first)
        
        
    def floor(self, key, height):
        node = self.roots[height]
        while node.next != None and node.next.key < key: 
            node = node.next
        return node

    
    def put(self, key, value):
        height = trailing_zeros(java_string_hash(key))
        #print(key, "-", value, "; H =",height)
        
        # update the value if key exists already
        bottomNode = self.roots[0]
        while bottomNode:
            if (bottomNode.key == key): 
                bottomNode.value = value
                return
            bottomNode = bottomNode.next
                
        # add new node in the table
        for i in range(0, height+1):
            newNode = Node()    
            newNode.value = value
            newNode.key = key
        
            node = self.floor(key, i)      
            newNode.next = node.next
            node.next = newNode  
    
    def get(self, key, height):
        node = self.roots[height]
        while node:
            if (node.key == key): return node
            node = node.next
        return Node()   
    
    def size(self):
        node = self.roots[0]
        i = 0
        while node:
            i+=1
            node = node.next
        return i
    
    def control(self, key , height):
        node = self.get(key, height)
        if(node.next== None): return None
        else: return node.next.key
        
    def _print(self):
        print()
        print("   Symbol table: ")
        for i in range(32,-1,-1):
            node = self.roots[i]
            if(node and node.next!=None): print("   HashPipe[",i+1,"]: ", end="")
            #if node.next: node = node.next
            while node and node.next != None:
                print(node, end="->")
                node = node.next
            if(node.value!=None): print(node)    
            
         
if len(sys.argv) > 1:
    try:
       sys.stdin = open(sys.argv[1])
    except IOError:
        print("File not found, using standard input instead")    
        
sTable = HashPipe()    
line = sys.stdin.readline()
keys = line.split()

'''
#Print Figure 3
for i in range (0, len(keys)):
    sTable.put(keys[i],i)
    print("Inserting : (",keys[i],",",i,")" )
    sTable._print()

'''


#codeJudge expected output / debugging code
for i in range (0, len(keys)):
    sTable.put(keys[i], i)
    print("Insert: ", keys[i])
    for g in range(i):
        cl = [ sTable.control(keys[g],h) for h in range(32) ]
        #print(cl)
        print( " ".join(x if x else '.' for x in cl) + "  : " + keys[g] )

   
print() 
print("Size of symbol table: ", sTable.size()-1)
sTable._print()










