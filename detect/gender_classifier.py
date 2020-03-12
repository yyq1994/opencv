from tensorflow.keras.models import load_model
import numpy as np
import cv2 as cv

# 加载人脸识别器
face_detector = cv.CascadeClassifier("D:\ProgramData\Anaconda3\pkgs\libopencv-3.4.2-h20b85fd_0\Library\etc\haarcascades\haarcascade_frontalface_default.xml")

# 加载性别分类模型
gender_classifier = load_model('simple_CNN.81-0.96.hdf5')

# 性别字典，用来返回性别
gender_label = {0:'female',1:'male'}


cap = cv.VideoCapture(0)

# 通过摄像头获取头像，检测人脸
#通过人脸判断性别，并展示
while cap.isOpened():
    ret,frame = cap.read()

    # 图像沿x轴翻转
    frame = cv.flip(frame,1)
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    # 检测人脸
    faces = face_detector.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=3,minSize=(140,140))

    # 通过人脸判断性别
    for (x,y,w,h) in faces:

        # 为了检测性别。上下大小分别加60，左右加30
        face = frame[(y-60):(y+h+60),(x-30):(x+w+30)]

        # 分类模型用的是（1,48,48,3），所以改变大小
        face = cv.resize(face,(48,48))
        face = np.expand_dims(face,0)

        # 归一化
        face = face/255.0

        # 返回性别代码，并根据上面性别字典返回性别
        gender_label_num = np.argmax(gender_classifier.predict(face))
        gender = gender_label[gender_label_num]

        # 框出人脸，并显示性别
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv.putText(frame,gender,(x,y),cv.FONT_HERSHEY_PLAIN,5,(255,255,255),3)

    cv.imshow('hei',frame)
    if cv.waitKey(1) & 0xff==27:
        break
cap.release()
cv.destroyAllWindows()

