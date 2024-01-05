def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, key):
    # Decryption is just encryption with a negative key
    return encrypt(text, -key)

# Example usage:
key = 13  # Choose the key used for encryption

# Input the encrypted code
user_input_encrypted_code = input("Enter the encrypted code: ")

# Now, let's decrypt the user-inputted encrypted code
decrypted_code = decrypt(user_input_encrypted_code, key)
print("Decrypted:", decrypted_code)