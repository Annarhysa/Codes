# 1. Write a function that returns the maximum of two numbers. (Use if loop)

def max_of_two_numbers(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2
max_of_two_numbers(4,5)

'''
2. Write a function called divisible that takes a number. ( Use if loop)
If the number is divisible by 3, it should return “Three”.
If it is divisible by 5, it should return “Five”.
If it is divisible by both 3 and 5, it should return “Three and Five”
Otherwise, it should return the same number.

'''

def divisible(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Three and Five"
    elif number % 3 == 0:
        return "Three"
    elif number % 5 == 0:
        return "Five"
    else:
        return number

divisible(15)

'''
3. Write a function for checking the speed of drivers. This function should have one  parameter: speed.
If the speed is less than 70, it should print “Ok”.
Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
If the driver gets more than 12 points, the function should print: “License suspended”
'''

def check_speed(speed):
    if speed < 70:
        print("Ok")
    else:
        demerit_points = (speed - 70) // 5
        if demerit_points <= 12:
            print("Points:", demerit_points)
        else:
            print("License suspended")

check_speed(100)

'''

4. Write a function(Use for loop) called Show Numbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print
0 EVEN
1 ODD
2 EVEN
3 ODD

'''

def show_numbers(limit):
    for num in range(limit + 1):
        if num % 2 == 0:
            print(num, "EVEN")
        else:
            print(num, "ODD")

show_numbers(3)

'''
5. Write a program using a while loop to check the number n is less than seven. If it is less than seven, print n is less than 7 and add 1 to n. If it is greater than 7,  print n is not less than 7.
Write the code for all the above questions with algorithms within 4 steps
'''
n =  int(input("Enter a number: "))
while n < 7:
    print("n is less than 7")
    n += 1
print("n is not less than 7")

# Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.
def print_prime_numbers(limit):
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

print_prime_numbers(10)

# Write a Python program  to find a Factorial of a Number using Loop
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print("Factorial of", number, "is:", factorial)