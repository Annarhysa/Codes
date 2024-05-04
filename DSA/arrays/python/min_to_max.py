t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    M = min(a)
    f = 0
    print(n-a.count(min(a)))
    t -= 1
