#Seperate numbers and letters and change ASCII
def separate_numbers_letters(input_string):
    numbers = ''.join(filter(str.isdigit, input_string))  # Extract numbers using filter and isdigit
    letters = ''.join(filter(str.isalpha, input_string))  # Extract letters using filter and isalpha
    return numbers, letters

# Example string
input_string = input("Choose your string")

# Separate numbers and letters
numbers, letters = separate_numbers_letters(input_string)

# Display the results
print("Numbers:", numbers)
print("Letters:", letters)

def convert_even_numbers_to_ascii(input_string):
    numbers = ''.join(filter(str.isdigit, input_string))  # Extract numbers using filter and isdigit
    letters = ''.join(filter(str.isalpha, input_string))  # Extract letters using filter and isalpha
    
    # Convert even numbers to ASCII decimal values
    numbers_ascii = ''.join([str(ord(num)) if int(num) % 2 == 0 else num for num in numbers])
    
    # Convert uppercase letters to ASCII decimal values
    letters_ascii = ''.join([str(ord(letter)) if letter.isupper() else letter for letter in letters])

    return numbers_ascii, letters_ascii

# Example string
input_string = "aBc123DeF456"

# Convert even numbers and uppercase letters
numbers_ascii, letters_ascii = convert_even_numbers_to_ascii(input_string)

# Display the results
print("Even Numbers as ASCII:", numbers_ascii)
print("Uppercase Letters as ASCII:", letters_ascii)