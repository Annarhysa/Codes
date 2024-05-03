#User function Template for python3


class Solution:
    def missingNumber(self,array,n):
        output = 0
        arr = []
        for i in range(1,n+1):
            arr.append(i)
        
        for i in arr:
            if i not in array:
                output = i
        return output


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends