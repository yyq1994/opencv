import cv2 as cv
import numpy as np
# 1. load xml
# 2. load jpg
# 3. haar gray
# 4. detect
# 5. draw

faces = cv.CascadeClassifier(r"haarcascade_frontalface_default.xml")
eyes = cv.CascadeClassifier(r'haarcascade_eye.xml')

# 2.加载图片

# 从摄像头获取视频
cap = cv.VideoCapture(0)
while cap.isOpened():
    ret,frame = cap.read()
         
    #3.灰度处理
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    #4.人脸检测
    face = faces.detectMultiScale(gray,1.3,5)  #1.gray_pic 2.比例缩放  3. 目标大小
    print('脸的个数{}'.format(len(face)))
    
    #5.框出人脸和眼睛
    for (x,y,w,h) in face:
        
        #对人脸画框
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        roi_face = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        
        #5. 检测眼睛
        eye = eyes.detectMultiScale(roi_face)  #灰度图像
        print('眼睛个数{}'.format(len(eye)))
        #框出眼睛
        for (ex,ey,ew,eh) in eye:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,255))
    #效果展示
    cv.imshow('lalala',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
