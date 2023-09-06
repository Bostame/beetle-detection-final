# ================================================================
#
#   File name   : write_orientation.py
#   Author      : Bostame Md Bayazid
#   Purpose      : For research module of masters course
#   Description : object detection image and video example
#
# ================================================================
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '1'
from yolov3.utils import Load_Yolo_model
from yolov3.object_location import detect_loc, tf
import glob

label_txt = '/home/mbostame/Documents/thesis_project/beetle_detection/beetle-detection/IMAGES/image_list_flower.txt'
imgdir = '/home/mbostame/Documents/thesis_project/beetle_detection/beetle-detection/IMAGES/flower'

filelist = [f for f in glob.iglob(imgdir + "**/**/**/*.jpg", recursive=True)]

yolo = Load_Yolo_model()

for ID in tf.range(len(filelist)-1):
    image_info = open(label_txt).readlines()[ID].split()
    image_path = image_info[0]
    detect_loc(yolo, image_path)
    if ID == len(filelist):
        break
