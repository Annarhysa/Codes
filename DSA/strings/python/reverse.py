def reverse_string(text):
    reversed_text = ''
    punctuation_marks = ',.!?;:'

    # Initialize pointers for reversing the string
    i = 0
    j = len(text) - 1

    # Iterate through the string from both ends
    while i <= j:
        # If the characters at the pointers are not alphabetic, move the pointers
        if not text[i].isalpha():
            reversed_text += text[i]
            i += 1
        elif not text[j].isalpha():
            reversed_text = text[j] + reversed_text
            j -= 1
        # If both characters are alphabetic, swap their positions and preserve case
        else:
            if text[i].islower():
                reversed_text += text[j].lower()
            else:
                reversed_text += text[j].upper()
            if text[j].islower():
                reversed_text += text[i].lower()
            else:
                reversed_text += text[i].upper()
            i += 1
            j -= 1

    return reversed_text

# Take user input
text = input()

# Reverse the string and print the result
print(reverse_string(text))
                                                                                                                            