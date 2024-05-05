def calculate_gifts(scores):
    gifts = [1] * len(scores)  # Initial gift count for each team member
    max_gift = 1  # Maximum gift count initialized to 1

    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:  # If current score is greater than previous score
            gifts[i] += 1  # Add one more gift
            max_gift = max(max_gift, gifts[i])  # Update maximum gift count
            if scores[i] % 3 == 0:  # Special condition: score divisible by 3
                gifts[i] += 3  # Add 3 extra gifts
            if scores[i] % 5 == 0:  # Special condition: score divisible by 5
                gifts[i] += 5  # Add 5 extra gifts
            if scores[i] % 7 == 0:  # Lucky draw: score divisible by 7
                gifts[i] += 1  # Add 1 more gift

        elif scores[i] < scores[i - 1]:  # If current score is less than previous score
            gifts[i] = 1  # Reset gift count to 1
            max_gift = max(max_gift, gifts[i])  # Update maximum gift count

        else:  # If scores are equal
            print("Should not receive the same number of gifts")
            return
        
    return gifts

# Take user input
scores = list(map(int, input().split()))

# Check for invalid input
if any(score < 0 for score in scores):
    print("Invalid input")
else:
    # Generate the gift count and output the result
    result = calculate_gifts(scores)
    if result:
        print(' '.join(map(str, result)))
                                                                                                                            