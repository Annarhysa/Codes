def find_highest_peaks(heights):
    # Ensure there are at least three elements in the list
    if len(heights) < 3:
        return "Invalid Input"

    # Validate input data types
    if not all(isinstance(height, int) for height in heights):
        return "Input was not in a correct format"

    # Identify peaks
    peaks = []
    for i in range(1, len(heights) - 1):
        if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
            peaks.append(heights[i])

    # Determine the highest peak
    if peaks:
        highest_peak = max(peaks)
        highest_peaks_count = peaks.count(highest_peak)

        return highest_peaks_count, [highest_peak] * highest_peaks_count
    else:
        return 0, []


# Function to parse input into a list of integers
def parse_input(input_str):
    try:
        return list(map(int, input_str.split()))
    except ValueError:
        return "Input was not in a correct format"


# Read input from standard input
import sys
input_str = sys.stdin.read().strip()

# Parse the input
heights = parse_input(input_str)

# If the input is invalid, print the error message
if isinstance(heights, str):
    print(heights)
else:
    # Get the highest peaks and the peak count
    result = find_highest_peaks(heights)

    if isinstance(result, str):
        print(result)
    else:
        num_peaks, highest_peaks = result
        print(num_peaks)
        print(" ".join(map(str, highest_peaks)))