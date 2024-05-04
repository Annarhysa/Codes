def min_steps_to_target(target, candies):
    candies.sort()  # Sort the candies in ascending order
    steps = 0  # Initialize the steps counter
    
    while len(candies) >= 2:
        if candies[0] >= target:
            break  # If the sweetness of the least sweet candy is already equal to or greater than the target, exit the loop
        
        # Calculate the sweetness of the new candy by combining the two least sweet candies
        new_candy_sweetness = candies[0] + 2 * candies[1]
        
        # Remove the two least sweet candies from the list
        candies = candies[2:]
        
        # Insert the new candy into the list while maintaining the ascending order
        for i in range(len(candies)):
            if new_candy_sweetness <= candies[i]:
                candies.insert(i, new_candy_sweetness)
                break
        else:
            candies.append(new_candy_sweetness)  # If new candy has the highest sweetness, append it at the end
            
        steps += 1  # Increment the steps counter
        
    return steps

# Take user input
target = int(input())
candies = list(map(int, input().split()))

# Output the result
print(min_steps_to_target(target, candies))
                                                                                                                            