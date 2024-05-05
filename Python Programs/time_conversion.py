def convert_to_military(time_str):
    # Split the time string into components
    time_components = time_str.split(':')
    hour = int(time_components[0])
    minute = time_components[1]
    second_ampm = time_components[2]
    
    # Check if it's PM
    if second_ampm[-2:] == 'PM':
        # If it's not exactly 12 PM, add 12 to the hour
        if hour != 12:
            hour += 12
    # If it's AM and exactly 12 AM, set hour to 0
    elif hour == 12:
        hour = 0
    
    # Convert hour to string and ensure it's formatted with leading zeros if needed
    hour_str = str(hour).zfill(2)
    
    # Concatenate the components to form the military time
    military_time = hour_str + ':' + minute + ':' + second_ampm[:2]
    
    return military_time

# User input
time_str = input()

# Convert the time to military format and print the result
print(convert_to_military(time_str))
                                                                                                                            