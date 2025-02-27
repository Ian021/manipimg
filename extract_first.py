from PIL import Image
import os

# Define the path to the input directory and the output directory
input_directory = './monsters'
output_directory = './'
output_image_path = os.path.join(output_directory, 'combined_image.png')

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Get a list of all image files in the input directory
image_files = [f for f in os.listdir(input_directory) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]

# List to hold cropped images
cropped_images = []

# Process each image file
for image_file in image_files:
    input_image_path = os.path.join(input_directory, image_file)
    with Image.open(input_image_path) as img:
        # Convert image to RGBA to handle transparency
        img = img.convert('RGBA')
        if 'dragon' in image_file.lower():
            # Crop the first 32x32 pixels and resize to 16x16
            cropped_img = img.crop((0, 0, 32, 32)).resize((16, 16), Image.Resampling.LANCZOS)
        else:
            # Crop the first 16x16 pixels
            cropped_img = img.crop((0, 0, 16, 16))
        cropped_images.append(cropped_img)

# Determine the size of the combined image
combined_width = 16 * len(cropped_images)
combined_height = 16

# Create a new blank image with the combined size and RGBA mode
combined_image = Image.new('RGBA', (combined_width, combined_height), (0, 0, 0, 0))

# Paste each cropped image into the combined image
for i, cropped_img in enumerate(cropped_images):
    combined_image.paste(cropped_img, (i * 16, 0), cropped_img)

# Save the combined image
combined_image.save(output_image_path)

print(f'Combined image saved to {output_image_path}')