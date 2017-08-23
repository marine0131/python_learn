#! usr/bin/env python
'''
 url request = 192.168.10.162:2333/?image=home/whj/gitrepo/python_learn/opencv_light_detection-master/images/oven_on.jpg&debug=true
 if debug is on, several images will generate in the input image dir
 return: true (detect red light)/false (no red light)
'''
import os
import numpy as np
import cv2
from bottle import route, run, request


def create_hue_mask(image, lower_color, upper_color):
    lower = np.array(lower_color, np.uint8)
    upper = np.array(upper_color, np.uint8)

    # Create a mask from the colors
    mask = cv2.inRange(image, lower, upper)
    output_image = cv2.bitwise_and(image, image, mask = mask)
    return output_image


def main(image_dir, output_dir):
    # Load image
    image = cv2.imread(image_dir)

    # Blur image to make it easier to detect objects
    blur_image = cv2.medianBlur(image, 3)
    if output_dir:
        result_image_path = os.path.join(output_dir, "blur_image.jpg")
        cv2.imwrite(result_image_path, blur_image)

    # Convert to HSV in order to
    hsv_image = cv2.cvtColor(blur_image, cv2.COLOR_BGR2HSV)
    if output_dir:
        result_image_path = os.path.join(output_dir, "hsv_image.jpg")
        cv2.imwrite(result_image_path, hsv_image)

    # Get lower red hue
    lower_red_hue = create_hue_mask(hsv_image, [0, 100, 100], [10, 255, 255])
    if output_dir:
        result_image_path = os.path.join(output_dir, "lower_red_hue.jpg")
        cv2.imwrite(result_image_path, lower_red_hue)

    # Get higher red hue
    higher_red_hue = create_hue_mask(hsv_image, [160, 50, 100], [179, 255, 255])
    if output_dir:
        result_image_path = os.path.join(output_dir, "higher_red_hue.jpg")
        cv2.imwrite(result_image_path, higher_red_hue)

    # Merge the images
    full_image = cv2.addWeighted(lower_red_hue, 1.0, higher_red_hue, 1.0, 0.0)
    if output_dir:
        result_image_path = os.path.join(output_dir, "full_image.jpg")
        cv2.imwrite(result_image_path, full_image)

    # Blur the final image to reduce noise from image, number in the () is the
    # blur window size
    full_image = cv2.GaussianBlur(full_image, (3, 3), 2, 2)
    if output_dir:
        result_image_path = os.path.join(output_dir, "full_image_blur.jpg")
        cv2.imwrite(result_image_path, full_image)

    # Convert image to gray in order to find circles in the image
    image_gray = cv2.cvtColor(full_image, cv2.COLOR_BGR2GRAY)
    if output_dir:
        result_image_path = os.path.join(output_dir, "full_image_gray.jpg")
        cv2.imwrite(result_image_path, image_gray)

    # Find circles in the image
    circles = cv2.HoughCircles(image_gray, cv2.cv.CV_HOUGH_GRADIENT, 2, 50, param1 = 160, param2 = 10)

    # If we didn't find circles, the oven status is "OFF"
    if circles is None:
        return "false"

    # If we did find circles, the oven is "ON"
    if output_dir:
        # Draw the circles on the original image
        circles = np.round(circles[0, :]).astype("int")
        for (center_x, center_y, radius) in circles:
            cv2.circle(image, (center_x, center_y), radius, (0, 255, 0), 4)
        result_image_path = os.path.join(output_dir, "original_image_with_circles.jpg")
        cv2.imwrite(result_image_path, image)

    return "true"


@route('/')
def index():
    image_dir = request.query.image
    debug = request.query.debug.upper()
    output_dir = None
    if debug == 'TRUE':
        dir_list = str(image_dir).split('/')
        if not dir_list[-1]:
            dir_list.pop()
        dir_list.pop()
        output_dir = '/'.join(dir_list)+'/'

    return main(image_dir, output_dir)

run(host='192.168.10.162', port=2333)
