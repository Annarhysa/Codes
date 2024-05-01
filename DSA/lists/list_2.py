# Write a python program to interchange first and last elements in a list.

def swapList(newList):
    size = len(newList)
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList

list  = [1,2,3,4,5,6]

print(swapList(list))

# Write a Python program to find N largest and smallest elements from the list

def maxel(list1, N):
    final_list = []
    for i in range(0, N):
        max1 = 0
        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j]
        list1.remove(max1)
        final_list.append(max1)
    return final_list


def minel(l, n):
    nSmallestList = []
    for i in range(n):
        nSmallestList.append(min(l))
        l.remove(min(l))
    return nSmallestList

list = [1,2,3,4,5,6,7,8,9]
print("Maximum two elements: ", maxel(list,2))
print("Minimum two elements: ", minel(list,2))

# Write a python program to find the cumulative sum of elements in a list

def Cumulative(lists):
    cu_list = []
    length = len(lists)
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]
    return cu_list[1:]

list = [1,2,3,4,5,6,7]

print(Cumulative(list))

# Write a python program to find positive numbers from a list.

def positive_num(list):
  for i in list:
    if (list[i]>=0):
      return list[i]

list = [-1,-2,-3,0, 4, -10]

print("The positive numbers form the list are as follows : " , positive_num(list))

# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

def printValues():
	l = []
	for i in range(1,31):
		l.append(i**2)
	print(l[:5])
	print(l[-5:])

printValues()

# Write a Python | Program to create two lists with EVEN numbers and ODD numbers from a list.

def splitevenodd(A):
   evenlist = []
   oddlist = []
   for i in A:
      if (i % 2 == 0):
         evenlist.append(i)
      else:
         oddlist.append(i)
   print("Even lists:", evenlist)
   print("Odd lists:", oddlist)

list = [2,3,5,6,7,10,11,23,46,77]
print(splitevenodd(list))

# Write a Python program to multiply all numbers of a list

def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

list = [2,3,6,7,8]
print(multiplyList(list))