def super_digit(n):
    # If the number has only one digit, return the number itself
    if len(n) == 1:
        return int(n)
    # Otherwise, calculate the sum of its digits recursively
    else:
        digit_sum = sum(int(digit) for digit in n)
        return super_digit(str(digit_sum))

# Input
number = input().strip()
repetitions = int(input().strip())

# Calculate the repeated number
repeated_number = number * repetitions

# Calculate the super digit of the repeated number
result = super_digit(repeated_number)

# Output the super digit
print(result)