def max_value_after_operations(size, queries):
    arr = [0] * size  # Initialize the array with zeros
    
    for query in queries:
        start_idx, end_idx, value = query
        # Update the array based on the query
        for i in range(start_idx - 1, end_idx):
            arr[i] += value
    
    # Find the maximum value in the array
    max_value = max(arr)
    return max_value

# Take user input
size = int(input())
query_count = int(input())

queries = []
for _ in range(query_count):
    query = list(map(int, input().split()))
    queries.append(query)

# Output the result
print(max_value_after_operations(size, queries))
                                                                                                                            