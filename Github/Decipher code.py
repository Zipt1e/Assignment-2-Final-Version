#Code to decipher text 
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  

# Check if the character is a letter
            shifted = ord(char) + shift 

# Shift the character by the given value
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
            result += chr(shifted)  
            
# Append the shifted character to the result
        else:
            result += char  
            
# Keep non-letter characters unchanged
    return result

# Example quote and shift value
quote = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQ NG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYY QBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
shift_value =13
# Apply Caesar cipher with the given shift value
ciphered_quote = caesar_cipher(quote, shift_value)

# Display the ciphered quote
print("Original Quote:", quote)
print("Ciphered Quote:", ciphered_quote)
