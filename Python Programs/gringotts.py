def last_remaining_element(arr):
    if any(num < 0 for num in arr):
        return "Array should only contain positive values"
    
    while len(arr) > 1:
        arr = arr[-1:] + arr[:-1]
        arr.pop()
    
    return arr[0]

# Take user input
arr = list(map(int, input().split()))

# Find the last remaining element after operations and output the result
print(last_remaining_element(arr))
                                                                                                                            