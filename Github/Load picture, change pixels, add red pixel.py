#Load picture 
from PIL import Image

# Open an image file
image = Image.open("C:/Users/scott/OneDrive/Desktop/chapter1.jpg")

#Add code to generate algorithm
import time

current_time = int(time.time())

generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

n=generated_number

print(n)

# Iterate through each pixel and modify RGB values
for y in range(image.height):
    for x in range(image.width):
        r, g, b = image.getpixel((x, y))


def modify_rgb(pixel, n):
    r, g, b = pixel
    # Modify each RGB component by adding 'n'
    new_r = r + n
    new_g = g + n
    new_b = b + n
    # Ensure the values are within the valid range (0-255)
    new_r = min(max(new_r, 0), 255)
    new_g = min(max(new_g, 0), 255)
    new_b = min(max(new_b, 0), 255)
    return new_r, new_g, new_b

# Iterate through each pixel and modify RGB values
width, height = image.size
for y in range(height):
    for x in range(width):
        pixel = image.getpixel((x, y))
        new_pixel = modify_rgb(pixel, n)
        image.putpixel((x, y), new_pixel)

# Save the modified image
output_path = 'chapter1out.png'
image.save(output_path)

# Show the image
image.show()

# Print a message indicating successful image generation
print(f"New image generated and saved as '{output_path}'")


#Loading the red pixel counter 
# Load the modified image
image_path = r'C:\Users\scott\chapter1out.png'
image = Image.open(image_path)

# Initialize a variable to store the sum of red pixel values
red_sum = 0

# Iterate through each pixel and calculate the sum of red values
width, height = image.size
for y in range(height):
    for x in range(width):
        r, _, _ = image.getpixel((x, y))  # Get the red component (r)
        red_sum += r  # Add red value to the sum

# Print the sum of all red pixel values
print(f"The sum of all red pixel values in the modified image is: {red_sum}")