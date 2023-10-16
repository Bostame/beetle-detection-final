import os
import glob
from PIL import Image
from tqdm import tqdm

Image.MAX_IMAGE_PIXELS = None  # to avoid image size warning

# Set the directory where your images are located
imgdir = '/home/mbostame/Documents/thesis_project/beetle_detection/beetle-detection/IMAGES/flower'

# Define the list of files you want to process (e.g., .jpg files)
filelist = [f for f in glob.glob(imgdir + "/**/*.jpg", recursive=True)]

# Specify the directory where you want to save the cropped images
savedir = "IMAGES/"

# Define the size of the patches
cropped_image_size = w, h = (512, 512)

# Define the stride for sliding the window (adjust as needed)
stride = (256, 256)

# Loop through each image file in the list
for file in filelist:
    img = Image.open(file)
    width, height = img.size

    frame_num = 1  # Initialize frame number

    # Loop through the image with overlapping patches based on the stride
    for col_i in tqdm(range(0, width - w + 1, stride[0])):
        for row_i in tqdm(range(0, height - h + 1, stride[1])):
            # Extract the patch
            crop = img.crop((col_i, row_i, col_i + w, row_i + h))

            # Get the directory and file name
            file_dir, file_name = os.path.split(file)
            name, extension = os.path.splitext(file_name)

            # Create a subdirectory based on the image file name
            sub_dir = os.path.join(savedir, name)
            os.makedirs(sub_dir, exist_ok=True)

            # Define the path to save the patch
            save_to = os.path.join(sub_dir, f"{name}_{frame_num:03}.jpg")

            # Save the cropped image
            crop.save(save_to)
            frame_num += 1  # Increment the frame number
