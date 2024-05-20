#User function Template for python3

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
            
    def enqueue(self,x):
        self.s1.append(x)
        
    def dequeue(self):
        
        #reverse the sequence
        while self.s1:
            self.s2.append(self.s1.pop())
        # store the result    
        result= self.s2.pop()
        
        #set it back to original sequence
        while self.s2:
            self.s1.append(self.s2.pop())
            
        return result

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        ob=Queue()
        n = int(input())
        a = list(map(int,input().strip().split()))
        i = 0
        while i<len(a):
            if a[i] == 1:
                ob.enqueue(a[i+1])
                i+=1
            else:
                print(ob.dequeue(),end=" ")
            i+=1

        print()
# } Driver Code Ends