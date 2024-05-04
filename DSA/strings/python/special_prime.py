import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_special_prime(limit):
    for i in range(limit - 1, 1, -1):
        if is_prime(i):
            for j in range(len(str(i))):
                for k in range(j + 1, len(str(i))):
                    num = int(str(i)[j] + str(i)[k])
                    if is_prime(num) and num < i:
                        return i
    return None

# Input
limit = int(input())

# Find the largest special prime number and output the result
special_prime = generate_special_prime(limit)
if special_prime is not None:
    print(special_prime)
                                                                                                                            