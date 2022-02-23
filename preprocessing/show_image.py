#================================================================
#   File name   : show_image.py
#   Author      : Bostame Md Bayazid
#   Purpose   : For research module of masters program
#   Description : show random image from created dataset
#================================================================
import random
import cv2
import numpy as np
from PIL import Image

#This is the code to show image from our automatic detected image
label_txt = "/home/mbostame/Documents/thesis_project/beetle_detection/beetle-detection/output.txt"
image_info = open(label_txt).readlines()[1].split()
image_path = "/IMAGES/test1/DSC03999_084.jpg"

image = cv2.imread(image_path)

for bbox in image_info[1:]:
    bbox = bbox.split(",")
    image = cv2.rectangle(image,(int(float(bbox[0])),
                                 int(float(bbox[1]))),
                                (int(float(bbox[2])),
                                 int(float(bbox[3]))), (255,0,0), 2)
image = Image.fromarray(np.uint8(image))
image.show()
