#================================================================
#
#   File name   : detection_custom.py
#   Author      : Bostame Md Bayazid
#   Purpose      : For research module of masters course
#   Description : object detection image and video example
#
#================================================================
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
from yolov3.utils import detect_image, Load_Yolo_model
from yolov3.object_location import detect_loc, tf
import random
import glob
import fnmatch

#imgdir = "D:/Thesis dataset/images/"

label_txt = "preprocessing/image_list.txt"
imgdir = "D:/Study_Materials/Research_module/Research/Beetles_Detection/IMAGES/test_dataset/"

filelist = [f for f in glob.glob(imgdir + "**/*.JPG", recursive=True)]

#filelist = len(fnmatch.filter(os.listdir(imgdir), '*.jpg'))

yolo = Load_Yolo_model()
for ID in tf.range(len(filelist)):
        image_info = open(label_txt).readlines()[ID].split()
        image_path = image_info[0]
        detect_loc(yolo, image_path)

        if ID == len(filelist):
            break



