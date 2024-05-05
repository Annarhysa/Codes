# 1.Write a Python program to count the number of characters (character frequency) in a string.

str1 = "RA2111047010144"
char_dict = dict()
for char in str1:
    count = str1.count(char)
    char_dict[char] = count
print(char_dict)

# 2.Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.

string= "Annarhysa Albert RA2111047010144"
count=0
for i in string:
      count=count+1
new=string[0:2]+string[count-2:count]
print("Newly formed string is:", new)

# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to &#39;$&#39;, except the first char itself.

str1 = "Annarhysa Albert"
char = str1[0]
str1 = str1.replace(char, '$')
str1 = char + str1[1:]
print(str1)

# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
a = "Annarhysa Albert"
b = "RA2111047010144"
new_a = b[:2] + a[2:]
new_b = a[:2] + b[2:]
print(new_a + ' ' + new_b)

# 5.Write a Python program to add &#39;ing&#39; at the end of a given string (length should be at least 3). If the given string already ends with &#39;ing&#39;, add &#39;ly&#39; instead.
# If the string length of the given string is less than 3, leave it unchanged.

str1 = "Annarhysa Albert RA2111047010144"
length = len(str1)
if length > 2:
    if str1[-3:] == 'ing':
        str1 += 'ly'
    else:
      str1 += 'ing'
print(str1)

# Write a Python program to find the first appearance of the substrings

str1 = "RA2111047010144 is not poor"
snot = str1.find('not')
spoor = str1.find('poor')
if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    print(str1)
else:
    print(str1)


# 7. Write a Python function that takes a list of words and return the longest word and the length of the longest one.

a = ["one", "two", "third", "four"]
max1 = len(a[0])
temp = a[0]
for i in a:
    if(len(i) > max1):
        max1 = len(i)
        temp = i
print("Longest word:", temp)
print("Lenght of the longest word: ", max1)


# Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).

items = ["Annarhysa Albert", "RA2111047010144", "SRM"]
print(",".join(sorted(list(set(items)))))

# Write a Python program to print the index of a character in a string.

str1 = "Annarhysa Albert"
for index, char in enumerate(str1):
    print("Current character", char, "position at", index )

# Write a Python program to count and display vowels in text.

string = "Annarhysa Albert RA2111047010144"
vowels = "AaEeIiOoUu"
final = [each for each in string if each in vowels]
print(len(final))
print(final)

