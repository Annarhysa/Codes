n1,n2 = map(int,input().split())
l = list(map(int,input().split(' ')))

count = 0

for i in l:
    if n1 == i:
        count = count + 1
    if n2 == i:
        count = count +1

if count == 2:
    print("YES")
else:
    print("NO")