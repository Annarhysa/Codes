import numpy as np

# Step 1: Create a matrix and fill it with random numbers
matrix = np.random.randint(0, 10, (5, 5))
print("Original Matrix:\n", matrix)

# Step 2: Sort the elements of the matrix in ascending order
matrix_sorted = np.sort(matrix)
arr = np.array(matrix_sorted)
print("Sorted Matrix:\n", arr)

# Step 3: Create two empty arrays to store the x and y coordinates of the sorted matrix elements
x_coords = []
y_coords = []

# Step 4: Traverse the sorted matrix and store the x and y coordinates of each element in their respective arrays
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] in matrix_sorted:
            x_coords.append(i)
            y_coords.append(j)
            matrix_sorted = np.delete(matrix_sorted, np.where(matrix_sorted==matrix[i][j]))

# Step 5: Initialize a variable to store the minimum distance between any two elements
min_distance = float("inf")

# Step 6: Traverse the x and y coordinate arrays and compute the distance between each pair of adjacent elements
for i in range(1, len(x_coords)):
    distance = np.sqrt((x_coords[i]-x_coords[i-1])**2 + (y_coords[i]-y_coords[i-1])**2)
    
    # Step 7: If the computed distance is less than the current minimum distance, update the minimum distance
    if distance < min_distance:
        min_distance = distance

# Step 8: Once all pairs of adjacent elements have been considered, return the minimum distance
print("Shortest Distance Between Two Elements:", min_distance)
