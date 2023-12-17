# Import the required modules
import os
import glob
from PIL import Image

# Define the source and destination directories
source_dir = "source" # Change this to your source directory
dest_dir = "destination" # Change this to your destination directory

# Create the destination directory if it does not exist
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Loop through the source directory and find all png, jpg and jpeg files
for file in glob.glob(source_dir + "/*.png") + glob.glob(source_dir + "/*.jpg") + glob.glob(source_dir + "/*.jpeg"):
    # Get the file name without extension
    file_name = os.path.splitext(os.path.basename(file))[0]
    # Open the image file with PIL
    image = Image.open(file)
    # Convert the image to RGB mode if it is not
    if image.mode != "RGB":
        image = image.convert("RGB")
    # Save the image as webp format in the destination directory with the same file name
    image.save(dest_dir + "/" + file_name + ".webp", "webp")
    # Close the image file
    image.close()
