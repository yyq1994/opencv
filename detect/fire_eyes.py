import cv2 as cv
import numpy as np
# -*- coding: utf-8 -*-
#步骤 1. load xml 2. load jpg 3. haar gray 4. detect 5. draw

faces = cv.CascadeClassifier(r"haarcascade_frontalface_default.xml")
eyes = cv.CascadeClassifier(r'haarcascade_eye.xml')

# 从摄像头获取视频
cap = cv.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()

    # 3.灰度处理
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # 4.人脸检测
    face = faces.detectMultiScale(gray, 1.3, 5)  # 1.gray_pic 2.比例缩放  3. 目标大小
    # 5.框出人脸和眼睛
    for (x, y, w, h) in face:
        roi_face = gray[y:y + int(h/2), x+int(w/2):x + w]
        roi_color = frame[y:y + int(h/2), x+int(w/2):x + w]

        # 5. 检测右眼
        right_eye = eyes.detectMultiScale(roi_face)  # 灰度图像
        print('右眼个数{}'.format(len(right_eye)))
        # 框出眼睛
        for (ex_r, ey_r, ew_r, eh_r) in right_eye:
            xx = np.random.randint(0,150)
            cv.line(roi_color,(xx,0),(int(ex_r+ew_r/2),int(ey_r+eh_r/2)),(0,0,255),10)
            cv.line(roi_color,(xx,0),(int(ex_r+ew_r/2),int(ey_r+eh_r/2)),(0,255,255),4)

        #5. 检测左眼
        roi_face = gray[y:y + int(h / 2), x :x + int(w/2)]
        roi_color = frame[y:y + int(h / 2), x :x + int(w/2)]
        left_eye = eyes.detectMultiScale(roi_face)  # 灰度图像
        print('右眼个数{}'.format(len(left_eye)))
        # 框出眼睛
        for (ex_l, ey_l, ew_l, eh_l) in left_eye:
            xx = np.random.randint(0,150)
            cv.line(roi_color,(xx,0),(int(ex_l+ew_l/2),int(ey_l+eh_l/2)),(0,0,255),10)
            cv.line(roi_color,(xx,0),(int(ex_l+ew_l/2),int(ey_l+eh_l/2)),(0,255,255),4)
    # 效果展示
    cv.imshow('fire', frame)
    if cv.waitKey(200) & 0xFF == 27:
        break
cap.release()
cv.destroyAllWindows()