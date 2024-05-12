# cook your dish here
t = int(input())

while t > 0:
    n = int(input())
    arr = input()
    ans = 0
    for i in range(0,n-1):
        if arr[i]=='0' and arr[i+1]=='0':
            ans+= 1
        elif arr[i]=='1' and arr[i+1]=='1':
            ans+= 1
    print(ans)
    t -= 1
