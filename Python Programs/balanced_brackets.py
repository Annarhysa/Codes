# Function to check if a given bracket is an opening bracket
def is_opening_bracket(char):
    return char in "({["

# Function to check if two brackets form a matching pair
def is_matching_pair(opening, closing):
    pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    return pairs[opening] == closing

# Function to check if a string of brackets is balanced and count the valid pairs
def check_balance_and_count(s):
    stack = []
    pair_count = 0
    
    for char in s:
        if is_opening_bracket(char):
            # Push opening bracket onto the stack
            stack.append(char)
        else:
            # If stack is empty, unmatched closing bracket
            if not stack:
                continue  # ignore unbalanced closing brackets
            # Pop the last opening bracket from the stack
            opening_bracket = stack.pop()
            if is_matching_pair(opening_bracket, char):
                # If they match, increment the pair count
                pair_count += 1
    
    # If there are unmatched opening brackets, string is unbalanced
    if stack:
        return "NO", pair_count
    
    # If everything is matched, it's balanced
    return "YES", pair_count

# Function to process the input and generate the output
def process_input(input_str):
    # Split input strings by commas
    bracket_strings = input_str.split(',')
    
    results = []
    for bracket_str in bracket_strings:
        result, pairs = check_balance_and_count(bracket_str)
        results.append(f"{result} {pairs}")
    
    return results

# Example input
input_str = input()

# Process input and get results
results = process_input(input_str)

# Print the results
for result in results:
    print(result)
