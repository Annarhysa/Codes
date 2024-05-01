# Write a Python script to sort (ascending and descending) a dictionary by value

import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1)))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)

'''
Write a Python Program to generate a temperature profile dictionary (values in range:30 to 100)for ten days randomly (from august 1 to august 31)
and check whether august 10 data exist in a dictionary or not. (Key=date,value=temperate value)

'''
import random
tempProf = {}
for i in range(11):
  x = random.randrange(1,31)
  y = random.randrange(30,100)
  tempProf[x]=y
print("Day\t\t Temperature")
for day,temp in tempProf.items():
  print("August ",day,"\t",temp)
flag = 10 in tempProf
if flag == False:
  print("Does not exist")
else:
  print('It exists')

# In program 2, find the count of temperature 30,40 in the dictionary. RA2111047010144

import random
tempProf = {}
c1=0
c2=0
for i in range(11):
  x = random.randrange(1,31)
  y = random.randrange(30,100)
  tempProf[x]=y
print("Day\t\t Temperature")
for day,temp in tempProf.items():
  print("August ",day,"\t",temp)
for a in tempProf:
  if tempProf[a] == 30:
    c1+=1
  if tempProf[a] == 40:
    c2+=1
print('Count of temperature 30 in the temperature profile is: ',c1)
print('Count of temperature 40 in the temperature profile is: ',c2)


'''
Repeat the program 2 for July month and write a python program to concatenate the two dictionaries into one dictionary named July_aug_temp.
'''

import random
from collections import defaultdict
tempProf_july = {}
tempProf_aug = {}
july_aug_temp = defaultdict(list)
for i in range(0,10):
  x = random.randint(1,31)
  y = random.randint(30,100)
  s1="July "+str(x)
  tempProf_july[s1]=y
  m = random.randint(1,31)
  n = random.randint(30,100)
  s2="August "+str(m)
  tempProf_aug[s2]=n
for tempProf in (tempProf_july, tempProf_aug):
  for key, value in tempProf.items():
    july_aug_temp[key].append(value)
print("Day\t\t Temperature")
for day,temp in july_aug_temp.items():
  print(day," \t",temp[0])


# Write a Python Program to multiply all the items in the dictionary “July_aug_temp '' which is generated in program 4 and find average temperature for the two months.

import random
from collections import defaultdict
tempProf_july = {}
tempProf_aug = {}
july_aug_temp = defaultdict(list)
sumTemp = 0
count = 0
for i in range(0,10):
  x = random.randint(1,31)
  y = random.randint(30,100)
  s1="July "+str(x)
  tempProf_july[s1]=y
  m = random.randint(1,31)
  n = random.randint(30,100)
  s2="August "+str(m)
  tempProf_aug[s2]=n
for tempProf in (tempProf_july, tempProf_aug):
  for key, value in tempProf.items():
    july_aug_temp[key].append(value)
print("Day\t\t Temperature")
for day,temp in july_aug_temp.items():
      print(day," \t",temp[0])
for days in july_aug_temp:
  sumTemp+=july_aug_temp[days][0]
  count+=1

avg=float(sumTemp)/count
print("The average temperature of july and august is %.2f"%avg)


'''
Write a python program that repeatedly asks the user to enter product names and prices.
Store all of them in a dictionary whose keys are product names and values are prices. And also write a code to search an item from the dictionary.
'''

dic = { }
while True :
    product = input("Enter the name of product (enter q for quit )= ")
    if product == "q" or product == "Q" :
        print()
        break
    else :
        price = int(input("Enter the price of product = "))
        dic [ product ] = price
while True :
    name = input("Enter the name of product those you have entered (enter q for quit )= ")
    if name == "q" or name == "Q" :
        break
    else :
        if name not in dic :
            print("Name of product is invalid")
            print()
        else :
            print("Price of product = ",dic[name])
            print()


# Write a Python program to get the maximum and minimum value in a dictionary.

points = {'Jake': 100, 'Andy': 450, 'Kate': 230}
print(max(points.values()))
print(min(points.values()))


