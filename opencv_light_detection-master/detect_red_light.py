#! usr/bin/env python
'''
 url request = 192.168.10.162:2333/?image=/home/whj/gitrepo/python_learn/opencv_light_detection-master/images/oven_on.jpg&debug=true
 if debug is on, several images will generate in the input image dir
 return: true (detect red light)/false (no red light)
'''
import os
import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt
from bottle import route, run, request
import json

def create_hue_mask(image, lower_color, upper_color):
    lower = np.array(lower_color, np.uint8)
    upper = np.array(upper_color, np.uint8)

    # Create a mask from the colors
    mask = cv2.inRange(image, lower, upper)
    output_image = cv2.bitwise_and(image, image, mask = mask)
    return output_image


def detect(image_dir, output_dir, debug_dir, color):
    # Load image
    image = cv2.imread(image_dir)

    # Blur image to make it easier to detect objects
    blur_image = cv2.medianBlur(image, 3)
    if debug_dir:
        result_image_path = os.path.join(debug_dir, color + "_blur_image.jpg")
        cv2.imwrite(result_image_path, blur_image)

    # Convert to HSV in order to
    hsv_image = cv2.cvtColor(blur_image, cv2.COLOR_BGR2HSV)
    if debug_dir:
        result_image_path = os.path.join(debug_dir, color + "_hsv_image.jpg")
        cv2.imwrite(result_image_path, hsv_image)

    if color == 'red':
        lower_hue_low = [0, 100, 100]
        lower_hue_high = [6, 255, 255]
        higher_hue_low = [156, 100, 100]
        higher_hue_high = [180, 255, 255]
    elif color == 'yellow':
        lower_hue_low = [0, 100, 100]
        lower_hue_high = [10, 255, 255]
        higher_hue_low = [156, 100, 100]
        higher_hue_high = [179, 255, 255]
    elif color == 'green':
        lower_hue_low = [35, 43, 43]
        lower_hue_high = [77, 255, 255]
        higher_hue_low = [78, 43, 43]
        higher_hue_high = [100, 255, 255]
    else:
        return 'unsupported color'

    # Get lower red hue
    lower_hue = create_hue_mask(hsv_image, lower_hue_low, lower_hue_high)
    if debug_dir:
        result_image_path = os.path.join(debug_dir, color + "_lower_hue.jpg")
        cv2.imwrite(result_image_path, lower_hue)

    # Get higher red hue
    higher_hue = create_hue_mask(hsv_image, higher_hue_low, higher_hue_high)
    if debug_dir:
        result_image_path = os.path.join(debug_dir, color + "_higher_hue.jpg")
        cv2.imwrite(result_image_path, higher_hue)

    # Merge the images
    full_image = cv2.addWeighted(lower_hue, 1.0, higher_hue, 1.0, 0.0)
    if debug_dir:
        result_image_path = os.path.join(debug_dir, color + "_full_image.jpg")
        cv2.imwrite(result_image_path, full_image)

    # Blur the final image to reduce noise from image, number in the () is the
    # blur window size
    #full_image = cv2.GaussianBlur(full_image, (7, 7), 2, 2)
    #if debug_dir:
    #    result_image_path = os.path.join(debug_dir, color + "_full_image_blur.jpg")
    #    cv2.imwrite(result_image_path, full_image)

    # Convert image to gray in order to find circles in the image
    image_gray = cv2.cvtColor(full_image, cv2.COLOR_BGR2GRAY)
    if debug_dir:
        result_image_path = os.path.join(debug_dir, color + "_full_image_gray.jpg")
        cv2.imwrite(result_image_path, image_gray)

    # Find circles in the image
    circles = cv2.HoughCircles(image_gray, cv2.cv.CV_HOUGH_GRADIENT, 2, 100, param1 = 100, param2 = 10, minRadius=0, maxRadius=20)

    # If we didn't find circles, the oven status is "OFF"
    if circles is None:
        return None

    # If we did find circles, the oven is "ON"
    if output_dir:
        # Draw the circles on the original image
        circles = np.round(circles[0, :]).astype("int")
        for (center_x, center_y, radius) in circles:
            cv2.circle(image, (center_x, center_y), radius, (0, 255, 0), 4)
        ff = image_dir.split('/')[-1].split('.')
        result_image_path = os.path.join(output_dir,  ff[0]+'_out.'+ff[1])
        cv2.imwrite(result_image_path, image)

    return len(circles)


if __name__ == '__main__':
    image_dir = '/home/whj/gitrepo/python_learn/opencv_light_detection-master/'
    output_dir = os.path.join(image_dir, 'output/')
    debug_dir = os.path.join(image_dir, 'debug/')
    color = 'red'
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    if not os.path.isdir(debug_dir):
        os.makedirs(debug_dir)

#     files = os.listdir(image_dir)
#     for image in files:
#         if len(image.split('.')) > 1:
#             print image + ':' +  detect(image_dir+image, output_dir)
    image = image_dir + sys.argv[1]
    print image + ':' +  str(detect(image, output_dir, debug_dir, color))

# @route('/')
# def index():
#     image_dir = request.query.image
#     debug = request.query.debug.upper()
#     root_dir = '/'.join(image_dir.split('/')[0:-1])
#     output_dir = os.path.join(root_dir, 'output/')
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)
#
#     debug_dir = None
#     if debug == 'TRUE':
#         debug_dir = os.path.join(root_dir, 'debug/')
#         if not os.path.exists(debug_dir):
#             os.makedirs(debug_dir)
#
#     result = {}
#     # detect red
#     color = 'red'
#     result[color] = detect(image_dir, output_dir, debug_dir, color)
#
#     return json.dumps(result)
#
# run(host='192.168.10.252', port=2333)
