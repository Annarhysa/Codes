#User function Template for python3

class Solution:

    def countWords(self, string):
        count = 0
        word = 0
        n = len(string)
        i = 0
        while i < n:
            if i < n - 1 and ((string[i] == '\\' and string[i + 1] == 'n') or (string[i] == '\\' and string[i + 1] == 't')):
                word = 0
                i += 1
            elif string[i] == ' ':
                word = 0
            elif word == 0:
                count += 1
                word = 1
            i += 1
        return count


                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.countWords(s))
# } Driver Code Ends