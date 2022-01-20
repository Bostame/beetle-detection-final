import os
import cv2
import glob
import tqdm


def annotation():
    class_lbl = 0
    images_path_list = glob.glob('data/source/*.JPG')
    for image_path in tqdm.tqdm(images_path_list):
        image_name = os.path.basename(image_path)
        print(image_name)
        im_name_without_ext = image_name.split('.')[0]
        img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        data_file = 'data/source/' + im_name_without_ext + ".txt"

        file = open(data_file, "r")
        data_str_list = file.readlines()
        data = []

        for d in data_str_list:
            d = d.strip('\n').strip('0')
            data.append([float(i) for i in d.split(' ') if i != ''])

        height = img.shape[0]
        width = img.shape[1]

        shape_width = 412
        shape_height = 412

        for idx, cord in enumerate(data):
            x_min, y_min, w, h = cord[0], cord[1], cord[2], cord[3]
            # w = x_max - x_min
            # h = y_max - y_min

            x, y = int((x_min + w / 2) * width), int((y_min + h / 2) * height)
            # x, y = int(x_min * width), int(y_min * height)

            if x - 412 < 0:
                x_left = 0
            else:
                x_left = x - 412

            if x + 412 > width:
                x_right = width
            else:
                x_right = x + 412

            if y - 412 < 0:
                y_bottom = 0
            else:
                y_bottom = y - 412

            if y + 412 > height:
                y_top = height
            else:
                y_top = y + 412

            crop_img = img.copy()[y_bottom:y_top, x_left:x_right]
            new_width = crop_img.shape[1]
            new_height = crop_img.shape[0]

            center_x = (x_min * width) - x_left - (w * new_width)
            center_y = (y_min * height) - y_bottom - (h * new_height)

            x_max = int(center_x + (w * width) / 2)
            y_max = int(center_y + (h * height) / 2)

            x_min = int(center_x - (w * width) / 2)
            y_min = int(center_y - (h * height) / 2)

            # start_point = (int(x_min), int(y_min))

            info = f'{class_lbl} {x_min / new_width} {y_min / new_height} {(x_max - x_min) / new_width} {(y_max - y_min) / new_height}'

            #cv2.rectangle(crop_img, (x_min, y_min), (x_min + (x_max - x_min), y_min + (y_max - y_min)), (0, 0, 255), 2)
            cv2.imwrite(f'data/images/{im_name_without_ext}_{idx}.JPG', crop_img)

            #file = open(f'data/images/{im_name_without_ext}_{idx}.txt', "w")
            #file.write(info)


if __name__ == '__main__':
    annotation()
