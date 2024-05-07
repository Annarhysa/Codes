#User function Template for python3

class Solution:
    def rotateMatrix(self, M, N, Mat):
        b = 0
        t = M-1
        l = 0
        r = N-1
        
        
        while b < t and l <r:
            temp = Mat[b+1][l]
            for x in range(l, r+1):
                temp, Mat[b][x] = Mat[b][x], temp
            b+=1
            
            for y in range(b, t+1):
                temp, Mat[y][r] = Mat[y][r], temp
            r-=1
            
            
            for x in range(r, l-1, -1):
                 temp, Mat[t][x] = Mat[t][x], temp
            t-=1
            
            for y in range(t, b-1, -1):
                temp, Mat[y][l] = Mat[y][l], temp
                
            l+=1
            
        return Mat


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        ans=ob.rotateMatrix(N,M,A)
        for i in range(N):
            for j in range(M):
                print(ans[i][j],end=" ")
            print()    
# } Driver Code Ends