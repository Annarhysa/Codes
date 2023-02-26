import math
def findPeak(arr, n):
    if(n==1):
        return 0
    if(arr[0] >= arr[1]):
        return 0
    if(arr[n-1]>=arr[n-2]):
        return n-1
    for i in range (1,n-1):
        if(arr[i]>=arr[i-1] and arr[i]>=arr[i+1]):
            return i

if __name__ == "__main__":

    arr = []
    n = int(input("Enter how many elements you want:"))
    print ('Enter numbers in array: ')
    for i in range(int(n)):
        a = input("Num :")
        arr.append(int(a))

    print("Index of a peak point is", findPeak(arr,n))
    print("The peak point is", arr[findPeak(arr,n)])
    print("Square root is", math.sqrt(arr[findPeak(arr,n)]))
