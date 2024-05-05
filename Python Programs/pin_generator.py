def generate_pin(numbers):
    pin = ''
    for num in numbers:
        num_sum = sum(int(digit) for digit in str(num))
        while num_sum > 9:
            num_sum = sum(int(digit) for digit in str(num_sum))
        if num_sum % 2 == 0:
            pin += str(num_sum)
        else:
            pin += chr(ord('a') + num_sum - 1)
    return pin

# Take user input
numbers = list(map(int, input().split()))

# Generate the PIN and output the result
print(generate_pin(numbers))
                                                                                                                            