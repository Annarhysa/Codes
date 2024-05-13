#User function Template for python3
class Solution:
	def commonSubseq(self, a, b):
		for i in range(len(a)):
			if a[i] in b:
				return 1
		return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		a, b = input().split()
		ob = Solution()
		if ob.commonSubseq (a, b):
			print (1)
		else:
			print (0)

	# Contributed By: Pranay Bansal
# } Driver Code Ends