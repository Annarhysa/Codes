def longest_substring_length(s):
    if not s:
        return 0
    
    max_length = 0
    start = 0
    char_index = {}
    
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        else:
            max_length = max(max_length, i - start + 1)
        char_index[char] = i
    
    return max_length

# Take user input
s = input()

# Find the length of the longest substring without repeating characters and output the result
print(longest_substring_length(s))
                                                                                                                            