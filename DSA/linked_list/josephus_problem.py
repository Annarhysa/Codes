#{ 
 # Driver Code Starts
import math



# } Driver Code Ends
#Complete this function

class Solution:
    def utilFunc(self, arr, k, index):
        if len(arr) == 1:
            return arr[0]
            
        # Calculating the index at which person would be killed.
        index = ((index+k-1)%len(arr))
        
        arr.pop(index)
        
        # Do the recursive call for n-1
        return self.utilFunc(arr, k, index)
        
    def josephus(self,n,k):
        #Your code here
        arr = []
        
        for i in range(1, n+1):
            arr.append(i)
            
        index = 0
        
        ans = self.utilFunc(arr, k, index)
        
        return ans

#{ 
 # Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        nk=[int(x) for x in input().strip().split()]
        n=nk[0]
        k=nk[1]
        
        print(Solution().josephus(n,k))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends