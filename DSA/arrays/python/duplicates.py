class Solution:
    def duplicates(self, arr, n): 
        present = False
        d = []
        
        for i in range(n-1):
            for j in range(i+1, n):
                if(arr[i] == arr[j]):
                    if arr[i] in d:
                        break
                    else:
                        d.append(arr[i])
                        present = True
            
        if present:
            d.sort()
            return d
        else:
            d.append(-1)
            return d
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends