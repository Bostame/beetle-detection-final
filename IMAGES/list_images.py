import os
import glob
from PIL import Image
from tqdm import tqdm
Image.MAX_IMAGE_PIXELS = None # to avoid image size warning

#imgdir = "D:/thesis_dataset/images/" #working directory
imgdir = '/home/mbostame/Documents/thesis_project/beetle_detection/beetle-detection/IMAGES/test1'
# if you want file of a specific extension (.png):
filelist = [f for f in glob.glob(imgdir + "**/**/*.jpg", recursive=True)]
savedir = "IMAGES/"




with open('../IMAGES/test_list.txt', "w", newline='\n') as file:
    file.write('\n'.join(map(str, filelist)))


'''
start_pos = start_x, start_y = (0, 0)
cropped_image_size = w, h = (512, 512)

for file in filelist:
    img = Image.open(file)
    width, height = img.size

    frame_num = 1
    for col_i in tqdm(range(0, width, w)):
        for row_i in tqdm(range(0, height, h)):
            crop = img.crop((col_i, row_i, col_i + w, row_i + h))
            name = os.path.basename(file)
            name = os.path.splitext(name)[0]
            save_to= os.path.join(savedir, name+"_{:03}.jpg")
            crop.save(save_to.format(frame_num))
            frame_num += 1
'''