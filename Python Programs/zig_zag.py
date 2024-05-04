def zigzag_sequence(nums):
    # Remove duplicates and sort the array
    nums = sorted(set(nums))
    n = len(nums)
    
    # Find k, where k is equal to (n+1)/2
    k = (n + 1) // 2
    
    # Initialize result array
    result = [0] * n
    
    # Fill the result array with elements in zigzag pattern
    for i in range(k):
        result[i * 2] = nums[i]
    for i in range(k, n):
        result[(i - k) * 2 + 1] = nums[i]
    
    return result

# Input
n = int(input().strip())  # Number of elements
nums = list(map(int, input().strip().split()))  # Elements of the array

# Find the lexicographically smallest zigzag sequence and output the result
result = zigzag_sequence(nums)
print(' '.join(map(str, result)))