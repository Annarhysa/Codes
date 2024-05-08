t = int(input())

while t > 0:
    n = int(input())
    arr = input()
    ans = ''
    for i in range(0,n,2):
        if arr[i]=='0' and arr[i+1]=='0':
            ans+='A'
        elif arr[i]=='0' and arr[i+1]=='1':
            ans+='T'
        if arr[i]=='1' and arr[i+1]=='0':
            ans+='C'
        if arr[i]=='1' and arr[i+1]=='1':
            ans+='G'
    print(ans)
    t -= 1
