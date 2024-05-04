from itertools import combinations

# Function to calculate the minimum and maximum values
def min_max_sum(numbers):
    # Generating all possible combinations of 4 numbers
    combinations_list = list(combinations(numbers, 4))
    
    # Calculating the sum of each combination
    sums = [sum(comb) for comb in combinations_list]
    
    # Finding the minimum and maximum sums
    min_sum = min(sums)
    max_sum = max(sums)
    
    return min_sum, max_sum

# Taking input from the user
numbers = list(map(int, input().split()))

# Getting the minimum and maximum values
min_value, max_value = min_max_sum(numbers)

# Printing the result
print(min_value, max_value)
                                                                                                                            