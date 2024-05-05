def caesar_cipher_encrypt(text, rotation):
    encrypted_text = ""
    for char in text:
        if 'A' <= char <= 'Z':
            encrypted_text += chr((ord(char) - ord('A') + rotation) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            encrypted_text += chr((ord(char) - ord('a') + rotation) % 26 + ord('a'))
        else:
            encrypted_text += char
    return encrypted_text

# Input
text = input().strip()  # Input string
rotation = 4  # Rotation for Caesar cipher

# Encrypt the input string and output the result
encrypted_text = caesar_cipher_encrypt(text, rotation)
print(encrypted_text)