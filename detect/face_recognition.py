import os
import cv2 as cv
import face_recognition
import numpy as np
import subprocess
from PIL import ImageDraw,Image,ImageFont
path = 'man'            #文件夹：我.jpg,张.jpg
cap = cv.VideoCapture(0)

# 姓名列表
total_names = []
# 人脸代码列表
total_face_encodings = []
nn = 0

# 统计存储的个人信息
for fn in os.listdir(path):
    print(path+'/'+fn)
    total_names.append(fn[:-4])
    face_encoding = face_recognition.face_encodings(face_recognition.load_image_file(path+'/'+fn))[0]
    total_face_encodings.append(face_encoding)

# 人脸识别
while cap.isOpened():
    ret,frame = cap.read()
    frame = cv.flip(frame,1)

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame,face_locations)

    # 所有人脸
    for (top,right,bottom,left),face_encoding in zip(face_locations,face_encodings):
        # 单个人脸对比
        name = '陌生人'
        for i,v in enumerate(total_face_encodings):
            match = face_recognition.compare_faces([v],face_encoding,tolerance=0.3)
            
            if match[0]:
                name = total_names[i]
            cv.rectangle(frame, (left, top), (right, bottom), (0, 255, 255))
            #检测是我，打开QQ
            if name =='我' and nn==0:
                subprocess.Popen('"D:\Program Files\Tencent\QQ\Bin\QQScLauncher.exe"')
                nn+=1
        frame = Image.fromarray(cv.cvtColor(frame, cv.COLOR_BGR2RGB))
        font = ImageFont.truetype('font/simsun.ttc', size=30, encoding='utf-8')
        draw = ImageDraw.Draw(frame)
        draw.text((left, top-35), name, (255,255,255), font)
        frame = cv.cvtColor(np.asarray(frame),cv.COLOR_RGB2BGR)
    cv.imshow('image',frame)
    if cv.waitKey(1) & 0xff==27:
        break

# 关闭窗口、释放内存
cap.release()
cv.destroyAllWindows()
