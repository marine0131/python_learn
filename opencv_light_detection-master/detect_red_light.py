#! usr/bin/env python
'''
 url request = 192.168.10.162:2333/
               ?image=/home/whj/gitrepo/python_learn/opencv_light_detection-master/images/oven_on.jpg
               &color=red,orange
               &debug=true

 if debug is on, several images will generate in the input image dir
 input:
     image= "file path"
     debug= True/False
     color= red,yellow  # use ',' split

return:
    {"orange": 2, "total": 12, "red": 10}

output file:
    IMAGENAME_out_red.jpg
'''
import os
import sys
import numpy as np
import cv2
from bottle import route, run, request
import json


def create_hue_mask(image, lower_color, upper_color):
    lower = np.array(lower_color, np.uint8)
    upper = np.array(upper_color, np.uint8)

    # Create a mask from the colors
    mask = cv2.inRange(image, lower, upper)
    output_image = cv2.bitwise_and(image, image, mask=mask)
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
        lower_hue_low = [0, 200, 50]
        lower_hue_high = [6, 255, 255]
        higher_hue_low = [156, 100, 50]
        higher_hue_high = [180, 255, 255]
    elif color == 'orange':
        lower_hue_low = [10, 200, 190]
        lower_hue_high = [14, 255, 240]
        higher_hue_low = [10, 200, 240]
        higher_hue_high = [15, 255, 240]
    elif color == 'yellow':
        lower_hue_low = [25, 43, 251]
        lower_hue_high = [31, 200, 255]
        higher_hue_low = [25, 43, 251]
        higher_hue_high = [31, 200, 255]
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
    full_image = cv2.GaussianBlur(full_image, (5, 5), 2, 2)
    if debug_dir:
        result_image_path = os.path.join(debug_dir, color + "_full_image_blur.jpg")
        cv2.imwrite(result_image_path, full_image)

    # Convert image to gray in order to find circles in the image
    image_gray = cv2.cvtColor(full_image, cv2.COLOR_BGR2GRAY)
    if debug_dir:
        result_image_path = os.path.join(debug_dir, color + "_full_image_gray.jpg")
        cv2.imwrite(result_image_path, image_gray)

    # Find circles in the image
    circles = cv2.HoughCircles(image_gray, cv2.cv.CV_HOUGH_GRADIENT, 2, 100, param1=300,
                               param2=10, minRadius=0, maxRadius=50)

    # If we didn't find circles, the oven status is "OFF"
    if circles is None:
        return 0

    height, width, channels = image.shape
    leng = 0
    # If we did find circles, the oven is "ON"
    if output_dir:
        # Draw the circles on the original image
        if color == 'yellow' or color == 'orange':
            circle_color = (0, 255, 0)
        else:
            circle_color = (0, 255, 255)
        circles = np.round(circles[0, :]).astype("int")
        for (center_x, center_y, radius) in circles:
            radius = radius if radius > 20 else 20
            if center_x > 0.01*width and center_x < 0.85*width and center_y > 0.15*height:
                cv2.circle(image, (center_x, center_y), radius, circle_color, 5)
                leng = leng+1
        ff = image_dir.split('/')[-1].split('.')
        result_image_path = os.path.join(output_dir,  ff[0]+'_out_'+color+'.'+ff[1])
        cv2.imwrite(result_image_path, image)

    return leng if leng > 0 else 0

# if __name__ == '__main__':
#     base_dir = os.path.abspath(os.curdir)
#     output_dir = os.path.join(base_dir, 'output/')
#     debug_dir = os.path.join(base_dir, 'debug/')
#     color = 'yellow'
#     if not os.path.isdir(output_dir):
#         os.makedirs(output_dir)
#     if not os.path.isdir(debug_dir):
#         os.makedirs(debug_dir)
#
#     f = os.path.join(base_dir,sys.argv[1])
#     if not os.path.exists(f):
#         print 'file not exist'
#     if os.path.isdir(f):
#         files = os.listdir(f)
#         for image in files:
#             image_dir = os.path.join(f, image)
#             print image + ': ' +  str(detect(image_dir, output_dir, debug_dir, color))
#     else:
#         for i in sys.argv[1:]:
#             image = i
#             print image + ':' +  str(detect(image, output_dir, debug_dir, color))


@route('/')
def index():
    image_dir = request.query.image
    debug = request.query.debug.upper()
    color = request.query.color
    root_dir = '/'.join(image_dir.split('/')[0:-1])
    output_dir = os.path.join(root_dir, 'output/')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    debug_dir = None
    if debug == 'TRUE':
        debug_dir = os.path.join(root_dir, 'debug/')
        if not os.path.exists(debug_dir):
            os.makedirs(debug_dir)

    result = {}
    # detect red
    if not color:
        color = 'red'
    color = color.split(',')
    total = 0
    for c in color:
        result[c] = detect(image_dir, output_dir, debug_dir, c)
        total = total + result[c]

    result['total'] = total
    return json.dumps(result)


run(host='127.0.0.1', port=2333)
