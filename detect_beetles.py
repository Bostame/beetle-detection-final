#================================================================
#
#   File name   : detect_beetles.py
#   Author      : Bostame Md Bayazid
#   Purpose      : For research module of masters course
#   Description : object detection image and video example
#
#================================================================
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '1'
import cv2
import numpy as np
import random
import time
import tensorflow as tf
from yolov3.yolov4 import Create_Yolo
from yolov3.utils import detect_image
from yolov3.configs import *

while True:
    ID = random.randint(0, 200)
    label_txt = "preprocessing/beetles_test.txt"
    image_info = open(label_txt).readlines()[ID].split()

    image_path = image_info[0]

    yolo = Create_Yolo(input_size=YOLO_INPUT_SIZE, CLASSES=TRAIN_CLASSES)
    yolo.load_weights(f"./checkpoints/{TRAIN_MODEL_NAME}") # use keras weights

    detect_image(yolo, image_path, "DSC07364_029.jpg", input_size=YOLO_INPUT_SIZE, show=True, CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0))
