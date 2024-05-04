def can_transform(start, end):
    if len(start) != len(end):
        return False
    
    # Iterate over both strings simultaneously
    i = 0  # Pointer for start string
    j = 0  # Pointer for end string
    while i < len(start) and j < len(end):
        # Skip 'X' characters in both strings
        while i < len(start) and start[i] == 'X':
            i += 1
        while j < len(end) and end[j] == 'X':
            j += 1
        
        # If one pointer reaches the end but the other hasn't, return False
        if (i < len(start) and j >= len(end)) or (i >= len(start) and j < len(end)):
            return False
        
        # Check if both characters at current positions are not equal
        if start[i] != end[j]:
            return False
        
        # Check if 'L' is moved to the left side
        if start[i] == 'L' and i < j:
            return False
        
        # Check if 'R' is moved to the right side
        if start[i] == 'R' and i > j:
            return False
        
        # Move pointers forward
        i += 1
        j += 1
    
    # After all checks, return True
    return True

# Input
start = input().strip()
end = input().strip()

# Output
print(can_transform(start, end))
                                                                                                                            