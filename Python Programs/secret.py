def number_of_people_aware_of_secret(n, delay, forget):
    # Array to count how many new people learn the secret each day
    daily_spread = [0] * (n + 1)

    # On the first day, one person discovers the secret
    daily_spread[1] = 1

    # The total number of people who know the secret on each day
    people_aware = 0

    # Iterate over each day
    for day in range(1, n + 1):
        # The number of new people who learn the secret on the current day
        new_people = daily_spread[day]

        # If the current day is the "forget" day, they forget the secret
        if day >= forget:
            people_aware -= daily_spread[day - forget]

        # If the current day is the "delay" day, they start sharing the secret
        if day + delay <= n:
            daily_spread[day + delay] += new_people
        
        # Update the total number of people who know the secret
        people_aware += new_people

    return people_aware


# Input reading
import sys
input_data = sys.stdin.read().split()

n = int(input_data[0])  # Number of days
delay = int(input_data[1])  # Delay before sharing
forget = int(input_data[2])  # Days after which people forget

# Get the result
result = number_of_people_aware_of_secret(n, delay, forget)

# Output the result
print(result)
