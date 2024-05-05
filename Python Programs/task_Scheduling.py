def is_feasible(tasks, workers, target):
    workers_used = 1
    current_workload = 0
    
    for task in tasks:
        if current_workload + task > target:
            workers_used += 1
            current_workload = task
            if workers_used > workers:
                return False
        else:
            current_workload += task
    
    return True

def min_time(tasks, workers):
    left = max(tasks)  # Minimum possible time is the maximum task duration
    right = sum(tasks)  # Maximum possible time is the total sum of task durations
    
    while left < right:
        mid = (left + right) // 2
        if is_feasible(tasks, workers, mid):
            right = mid
        else:
            left = mid + 1
    
    return left

# Input
N = int(input().strip())  # Number of tasks
tasks = list(map(int, input().strip().split()))  # Task durations
K = int(input().strip())  # Number of workers

# Calculate and output the minimum time required
print(min_time(tasks, K))