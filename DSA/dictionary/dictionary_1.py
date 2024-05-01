# Exercise 1: Convert two lists into a dictionary

keys = ["Ananrhysa Albert", "Raspberry pi"]
values = [144, "Sem 5th"]

res = {}
for key in keys:
    for value in values:
        res[key] = value
        values.remove(value)
        break

# Printing resultant dictionary
print("Resultant dictionary is : " + str(res))

# Exercise 2: Merge two Python dictionaries into one
def Merge(dict1, dict2):
    res = dict1 | dict2
    return res

dict1 = {'Annarhysa': "Albert"}
dict2 = {'Roll No.' : "RA2111047010144"}

print(Merge(dict1, dict2))

# Exercise 3: Print the value of key ‘history’ from the below dict

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']['history'])

# Exercise 4: Initialize dictionary with default values

name = ['Annarhysa', 'Albert']
value = {"Rollno": 'RA2111047010144', "Sub": "Raspbery Pi"}
res = dict.fromkeys(name, value)
print(res["Annarhysa"])

# Exercise 5: Create a dictionary by extracting the keys from a given dictionary

sample_dict = {
    "name": "Annarhysa Albert",
    "age": 19,
    "RollNo": "RA2111047010144"}
keys = ["name", "RollNo"]
newDict = {k: sample_dict[k] for k in keys}
print(newDict)


# Exercise 6: Delete a list of keys from a dictionary

sample_dict = {
    "name": "Annarhysa Albert",
    "age": 19,
    "RollNo": "RA2111047010144"}
keys = ["name", "RollNo"]
for k in keys:
    sample_dict.pop(k)
print(sample_dict)


# Exercise 7: Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}

bool = 200 in sample_dict.values()
if bool:
  print('200 present in dict')
else:
  print('200 not present in dict')

# Ezercise 8: Rename a key of a dictionary
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

# Exercise 9: Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

min(sample_dict, key=sample_dict.get)

# Exercise 10: Change value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']['salary'] = 8500
print(sample_dict)

# Exercise 11: Python program to iterate over dictionaries using for loops.
statesAndCapitals = {
	'Gujarat': 'Gandhinagar',
	'Maharashtra': 'Mumbai',
	'Rajasthan': 'Jaipur',
	'Bihar': 'Patna'
}

print('List Of given states and their capitals:\n')

for state, capital in statesAndCapitals.items():
	print(state, ":", capital)


# Exercise 12: Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
n = 5
list1 = []
list2 = []
for i in range(1,n+1):
  list1.append(i)
  list2.append(i*i*i)
result = dict(zip(list1,list2))
print(result)


# Exercise 13: Python program to map two lists into a dictionary.
keys = [1,2,3,4]
values = ['Interstellar','TDK','Inception','Oppenheimer']

res = dict(map(lambda i,j : (i,j) , keys,values))
print(res)


# Exercise 14: Python program to remove duplicates from the dictionary.
test_dict = {'Annarhysa': 10, 'Albert': 20, 'RA2111047010144': 20}
temp = []
res = dict()

for key, val in test_dict.items():

	if val not in temp:
		temp.append(val)
		res[key] = val

print("The dictionary after values removal : " + str(res))


# Exercise 15: Python program to find the highest 3 values of corresponding keys in a dictionary
my_dict = {'A': 67, 'B': 23, 'C': 45,
		'D': 56, 'E': 12, 'F': 69}

print("Initial Dictionary:")
print(my_dict, "\n")

print("Dictionary with 3 highest values:")
print("Keys: Values")

x=list(my_dict.values())
d=dict()
x.sort(reverse=True)
x=x[:3]
for i in x:
	for j in my_dict.keys():
		if(my_dict[j]==i):
			print(str(j)+" : "+str(my_dict[j]))
