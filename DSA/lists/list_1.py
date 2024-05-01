# Concatenate two lists index-wise
test_list1 = ['Annarhysa', 'Albert']
test_list2 = ['RA', '2111047010144']
for i in test_list2 :
	test_list1.append(i)
print ("Concatenated list : " + str(test_list1))

# Given a Python list of numbers. Turn every item of a list into its square

aList=[1,2,3,4,5,6,7]
print([i**2 for i in aList])

# Concatenate two lists in the following order

test_list1 = ['Annarhysa ', 'RA']
test_list2 = ['Albert', '2111047010144']
res = [i + j for i, j in zip(test_list1, test_list2)]
print(res)

# Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order

test_list1 = ['Annarhysa ', 'RA']
test_list2 = ['2111047010144', 'Albert']
for x, y in zip(test_list1, test_list2[::-1]):
    print(x, y)

# Remove empty strings from the list of strings

test_list1 = ["Annarhysa", "", "Albert", "RA", "", "2111047010144"]
res = list(filter(None, test_list1))
print(res)

# Given two strings, s1 and s2, create a new string by appending s2 in themiddle of s1

s1 ="Annarhysa  Albert"
s2 = "RA2111047010144"
mi = int(len(s1) / 2) + 2
x = s1[:mi:]
x = x + s2
x = x + s1[mi:]
print("After appending new string in middle:", x)

# Given two strings, s1, and s2 return a new string made of the first, middle, and last characters each input string

s1 ="Annarhysa Albert"
s2 = "RA2111047010144"
first_char = s1[0] + s2[0]
middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]
last_char = s1[len(s1) - 1] + s2[len(s2) - 1]
res = first_char + middle_char + last_char
print(res)


# Find all occurrences of “USA” in a given string ignoring the case

str1 = "Hi I am Annarhysa Albert. Annarhysa Albert is a very fun-loving enthusiast of Machine Learning"
sub_string = "Annarhysa Albert"
temp_str = str1.lower()
count = temp_str.count(sub_string.lower())
print("Occurrence count: ",count)

