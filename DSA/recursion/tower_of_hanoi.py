# User function Template for python3

class Solution:
    def toh(self, N, s, to, aux):
        steps = 0
        if N==1:
            print(f"move disk {N} from rod {s} to rod {to}")
            return 1
        steps = self.toh(N-1,s,aux,to)
        print(f"move disk {N} from rod {s} to rod {to}")
        steps += 1
        steps += self.toh(N-1,aux,to,s)
        return steps


#{ 
 # Driver Code Starts
# Initial Template for Python 3


import math


def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        ob = Solution()
        print(ob.toh(N, 1, 3, 2))
        T -= 1
if __name__ == "__main__":
    main()


# } Driver Code Ends