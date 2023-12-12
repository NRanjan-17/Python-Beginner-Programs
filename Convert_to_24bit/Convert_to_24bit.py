# pip install pillow
from PIL import Image
import os
import glob
# Specify the source folder where the PNG files are located
source_folder = 'source'
# Specify the destination folder where the converted images will be saved
destination_folder = 'destination'
# Create the destination folder if it does not exist
if not os.path.exists (destination_folder):
    os.makedirs (destination_folder)
# Loop through all the PNG files in the source folder
for file in glob.glob (os.path.join (source_folder, '*.png')):
    # Load the image
    img = Image.open (file)
    # Print the mode of the image
    print (img.mode)
    # Convert to 24-bit RGB mode
    img = img.convert ('RGB')
    # Print the mode of the image
    print (img.mode)
    # Get the file name without extension
    file_name = os.path.splitext (os.path.basename (file)) [0]
    # Create the new file path with the same name but in the destination folder
    new_file = os.path.join (destination_folder, file_name + '.png')
    # Save the image
    img.save (new_file)
