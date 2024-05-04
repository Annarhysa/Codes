def divisible_sum_pairs(divisor, arr):
    count = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] + arr[j]) % divisor == 0:
                count += 1
    
    return count

# Take user input
divisor = int(input())
arr = list(map(int, input().split()))

# Find the number of pairs and output the result
print(divisible_sum_pairs(divisor, arr))
                                                                                                                            