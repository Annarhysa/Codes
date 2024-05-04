import sys
def doSomething(inval):
    outval = []
    max_chunk = -1
    
    for num in inval:
        if num> max_chunk:
            if outval:
                print(''.join(map(str, outval)))
                outval = []
            max_chunk = num
        outval.append(num)
        
    if outval:
        print(''.join(map(str, outval)))
        
inputVal = list(map(int, input().split()))    
doSomething(inputVal)