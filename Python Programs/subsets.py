def subsets(nums):
    result = [[]]  # Start with an empty subset
    for num in nums:
        result += [curr + [num] for curr in result]  # Add subsets with the current number
    return result

# Input
nums = list(map(int, input().split()))

# Generate subsets
result = subsets(nums)

# Print subsets
for subset in result:
    print(' '.join(map(str, subset)))