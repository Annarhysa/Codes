from collections import Counter

def most_common_plant(sightings):
    # Count the occurrences of each plant ID
    plant_counts = Counter(sightings)
    
    # Sort the plant counts by frequency and plant ID
    sorted_plant_counts = sorted(plant_counts.items(), key=lambda x: (-x[1], x[0]))
    
    # Return the plant ID with the highest frequency
    return sorted_plant_counts[0][0]

# Take user input
sightings = list(map(int, input().split()))

# Find the most common plant ID and output the result
print(most_common_plant(sightings))
                                                                                                                            