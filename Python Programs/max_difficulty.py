# Function to process the queries and return the maximum total difficulty for each query
def max_difficulty(N, D, L, queries):
    results = []

    # Check constraints
    if not (1 <= N <= 10):
        return ["Invalid"]
    if not all(1 <= d <= 50 for d in D):
        return ["Invalid"]
    if not all(1 <= l <= 50 for l in L):
        return ["Invalid"]
    if not all(1 <= k <= N for k in queries):
        return ["Invalid"]

    # Combine difficulties and time limits into a list of tuples
    problem_info = list(zip(D, L))

    # For each query, find the maximum total difficulty
    for k in queries:
        # Sort by time limit in descending order
        problem_info_sorted = sorted(problem_info, key=lambda x: x[1], reverse=True)

        # Take the top `k` problems based on time limits
        top_problems = problem_info_sorted[:k]

        # Calculate the total difficulty for these top problems
        total_difficulty = sum(problem[0] for problem in top_problems)

        # Add the result to the list
        results.append(total_difficulty)

    return results


# Read input
D = list(map(int, input().split()))
L = list(map(int, input().split()))
queries = list(map(int, input().split()))

# Determine the number of problems (N) and number of queries (Q)
N = len(D)

# Get the results for the queries
results = max_difficulty(N, D, L, queries)

# Print the results
for result in results:
    print(result)
