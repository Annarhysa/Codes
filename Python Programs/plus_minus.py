def count_ratios(arr):
    # Count the total number of elements
    total_elements = len(arr)
    
    # Count the number of positive, negative, and zero elements
    positive_count = sum(1 for num in arr if num > 0)
    negative_count = sum(1 for num in arr if num < 0)
    zero_count = sum(1 for num in arr if num == 0)
    
    # Calculate the fractions
    positive_ratio = positive_count / total_elements
    negative_ratio = negative_count / total_elements
    zero_ratio = zero_count / total_elements
    
    # Print the fractions with three decimal places
    print("{:.3f}".format(positive_ratio))
    print("{:.3f}".format(negative_ratio))
    print("{:.3f}".format(zero_ratio))

# Take user input for the array
n = int(input())
arr = list(map(int, input().split()))

# Call the function with user input array
count_ratios(arr)
                                                                                                                            