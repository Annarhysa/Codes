# Write a  Python program to perform arithmetic operations on two integers.

a = int(input("enter integer 1: "))
b = int(input("enter integer 2: "))
print("The sum: ", a+b)
print("The difference: ", abs(a+b))
print("The product: ", a*b)
print("The division: ", a/b)

# Write a Python Program to find the area of a triangle.

a = int(input("enter the height of the triangle: "))
b = int(input("enter the base of the triangle: "))

print("the area of the triangle: ", (a*b)/2)

# Write a Python code to remove 6 characters from start of given string “Embedded Systems”

string = "Embedded system"
l = len(string)
print(string[6:l])

# Write the Python code to find the length of String “Computer Science”. Replace science with Electronics.

string = "Computer Science"
l = len(string)

print("Lenght of the string: ", l)

string_new = string[:8] + " Electronics"

print("New String: ", string_new)

# Write the Python program to reverse a string from user input

def reverse(s):
    string = ""
    for i in s:
        string = i + string
    return string

s = str(input("Enter a sentence of your choice: "))
reverse(s)