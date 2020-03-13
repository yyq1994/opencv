import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while cap.isOpened():
    _,frame = cap.read()
    hsv = frame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lower_blue = np.array([0, 0, 221])
    upper_blue = np.array([180, 30, 255])

    mask = cv.inRange(hsv,lower_blue,upper_blue)
    res = cv.bitwise_and(frame,frame,mask=mask)
    cv.imshow('image',res)
    cv.imshow('mask',mask)
    res = cv.GaussianBlur(res,(3,3),1)
    cv.imshow('GassianBlur',res)
    if cv.waitKey(1) & 0xff ==27:
        break
cap.release()
cv.destroyAllWindows()


# 如何找到颜色的hsv的值

# green=np.uint8([[[0,255,0]]])
# hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
# print hsv_green
# [[[60 255 255]]]