import numbers

import cv2
import tqdm
from yolov3.utils import image_preprocess, postprocess_boxes, nms, drop, replace_comma
from yolov3.yolov4 import *
import itertools
from itertools import groupby


def detect_loc(Yolo, image_path, input_size=512,
               score_threshold=0.3, iou_threshold=0.5):
    original_image = cv2.imread(image_path)
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

    image_data = image_preprocess(np.copy(original_image), [input_size, input_size])
    image_data = image_data[np.newaxis, ...].astype(np.float32)

    if YOLO_FRAMEWORK == "tf":
        pred_bbox = Yolo.predict(image_data)
    elif YOLO_FRAMEWORK == "trt":
        batched_input = tf.constant(image_data)
        result = Yolo(batched_input)
        pred_bbox = []
        for key, value in result.items():
            value = value.numpy()
            pred_bbox.append(value)

    pred_bbox = [tf.reshape(x, (-1, tf.shape(x)[-1])) for x in pred_bbox]
    pred_bbox = tf.concat(pred_bbox, axis=0)

    bboxes = postprocess_boxes(pred_bbox, original_image, input_size, score_threshold)
    bboxes = nms(bboxes, iou_threshold, method='nms')
    bbox2 = list(itertools.chain(*bboxes))  # added to make our 2D array to a 1D array
    bbox2 = drop(bbox2, 5)
    bbox2 = list(map(int, bbox2))  # added to make the list of float values to integer
    check = bbox2
    save_text = replace_comma(bbox2, image_path)
    print(save_text)

    if any(isinstance(value, numbers.Number) for value in check):
        with open('/home/mbostame/Documents/thesis_project/beetle_detection/beetle-detection/output.txt', 'a') as file:
            file.write(save_text)
