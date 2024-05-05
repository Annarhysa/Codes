t = int(input())

for i in range(t):
    n = int(input())
    n_list = []
    for j in range(n):
        e = int(input())
        n_list.append(e)
        
    n_list.sort()
    
    print(n_list[n-1])