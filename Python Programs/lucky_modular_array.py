def triple_modular_exponentiation(a, b, c, m):
    return ((pow(a, b, m) * pow(a, c, m)) % m) * pow(a, c, m) % m

def find_lucky_array(arr):
    n = len(arr)
    
    # Check if array length is less than 4
    if n < 4:
        return "Invalid Input"
    
    max_modulo = -1
    lucky_array = []
    
    # Iterate through all consecutive subarrays of length 4
    for i in range(n - 3):
        subarray = arr[i:i+4]
        sorted_subarray = sorted(subarray)
        modulo_value = triple_modular_exponentiation(sorted_subarray[0], sorted_subarray[1], sorted_subarray[2], sorted_subarray[3])
        
        if modulo_value > max_modulo:
            max_modulo = modulo_value
            lucky_array = subarray
        elif modulo_value == max_modulo and subarray != lucky_array:
            return "There is more than one lucky arrays"
    
    return lucky_array, max_modulo

# Take user input
arr = list(map(int, input().split()))

# Find the lucky array and output the result
result = find_lucky_array(arr)
if isinstance(result, tuple):
    lucky_array, max_modulo = result
    print(*lucky_array)
    print(max_modulo)
else:
    print(result)
                                                                                                                            