import sys

def doSomething(inval):
    n = len(inval)
    outval = 0
    
    for i in range(n):
        for j in range(n):
            x = inval[i]
            y = inval[j]
            count = 0
            
            while x>0 or y>0:
                if x%2 == y%2:
                    count +=1
                
                x//=2
                y//=2
            
            outval += count
    return outval*2

input = list(map(int, input().split()))
#input = int(input())
output = doSomething(input)
print (output)