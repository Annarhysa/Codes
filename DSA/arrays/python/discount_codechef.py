t = int(input())

while t > 0:
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    s = 0
    new_sum = 0
    new = []
    for i in a:
        s = s+i
        d = i - y
        if d<0:
            new.append(0)
        else:
            new.append(d)
    
    for i in new:
        new_sum = i+new_sum
    
    if(new_sum+x<s):
        print("COUPON")
    else:
        print("NO COUPON")
        
