def check_sorted_columns(grid):
    n = len(grid)
    m = len(grid[0])
    
    for j in range(m):
        column = [grid[i][j] for i in range(n)]
        if column != sorted(column):
            return "NO"
    return "YES"

def rearrange_rows(grid):
    return ["".join(sorted(row)) for row in grid]

def grid_challenge(records):
    results = []
    for record in records:
        _, size, *chars = record.split(',')
        rows, cols = map(int, size.split())
        grid = [chars[i:i+cols] for i in range(0, rows*cols, cols)]
        sorted_rows = rearrange_rows(grid)
        results.append(check_sorted_columns(sorted_rows))
    return results

# Take user input
num_records = int(input())
records = []
for _ in range(num_records):
    record = input()
    records.append(record)

# Process and print results
results = grid_challenge(records)
for result in results:
    print(result)
                                                                                                                            