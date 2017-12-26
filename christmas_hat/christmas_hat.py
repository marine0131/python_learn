#! usr/bin/env python

import cv2
import dlib

hat_img = cv2.imread("hat.png", cv2.IMREAD_UNCHANGED)
img = cv2.imread("photo.jpg")

r,g,b,a = cv2.split(hat_img)
rgb_hat = cv2.merge((r,g,b))

cv2.imwrite("hat_alpha.jpg",a)

# dlib face feature detect
predictor_path = "shape_predictor_5_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_path)

detector = dlib.get_frontal_face_detector()

dets = detector(img, 1)


if len(dets) > 0:
    for d in dets:
        x,y,w,h = d.left(),d.top(),d.right()-d.left(), d.bottom()-d.top()
        shape = predictor(img, d)
        # draw cirlces of 5 features
        # cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2,8,0)
        # for point in shape.parts():
        #    cv2.circle(img, (point.x, point.y), 3, color=(0,255,0))

        # cv2.imshow("image", img)
        # cv2.waitKey()

        # pick left and right eyes
        p1 = shape.part(0)
        p2 = shape.part(2)
        eyes_center = ((p1.x+p2.x)//2, (p1.y+p2.y)//2.0)

        # resize the hat
        factor = 1.2
        r_hat_w = int(round(w*factor))  #adjust hat width to 1.5*facewidth
        r_hat_h = int(round(rgb_hat.shape[0]*w/rgb_hat.shape[1]*factor))  #adjust hat height

        if r_hat_h > y:  # hat height > blank space above face top
            r_hat_h = y-1

        resized_hat = cv2.resize(rgb_hat, (r_hat_w, r_hat_h))  # resize hat size


        # dift of hat
        dh = 0
        dw = 0
        # cut a image from img
        bg_roi = img[y+dh-r_hat_h: y+dh, (eyes_center[0]-r_hat_w//3):(eyes_center[0]+r_hat_w//3*2)]
        bg_roi = bg_roi.astype(float)

        # get alpha as mask
        mask = cv2.resize(a, (r_hat_w, r_hat_h))  # resize alpha chanel
        mask_inv = cv2.bitwise_not(mask)  # reverse to make hat transparent
        mask_inv = cv2.merge((mask_inv, mask_inv, mask_inv))  # merge as rgb image
        alpha = mask_inv.astype(float)/255
        alpha = cv2.resize(alpha, (bg_roi.shape[1], bg_roi.shape[0]))

        # generate a black hat with upper face
        bg = cv2.multiply(alpha, bg_roi)
        bg = bg.astype("uint8")
        cv2.imwrite('bg.jpg', bg)

        # rgb hat
        hat = cv2.bitwise_and(resized_hat, resized_hat, mask=mask)
        cv2.imwrite('hat.jpg', hat)

        # add bg and rgb hat
        hat = cv2.resize(hat, (bg_roi.shape[1], bg_roi.shape[0]))
        add_hat = cv2.add(bg, hat)

        # repalce part of img with add_hat
        img[y+dh-r_hat_h : y+dh, (eyes_center[0]-r_hat_w//3):(eyes_center[0]+r_hat_w//3*2)] = add_hat

    # cv2.imshow('img',img)
    # cv2.waitKey()
    cv2.imwrite('final.jpg', img)

else:
    print("oops! no face detected")
