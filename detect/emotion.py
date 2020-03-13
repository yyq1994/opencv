#coding=utf-8
#表情识别

import cv2
from tensorflow.keras.models import load_model
import numpy as np

emotion_classifier = load_model('simple_CNN.530-0.65.hdf5')

emotion_labels = {
    0: 'angry',
    1: 'hate',
    2: 'fear',
    3: 'happy',
    4: 'sad',
    5: 'surprise',
    6: 'calm'
}

face_classifier = cv2.CascadeClassifier("D:\ProgramData\Anaconda3\pkgs\libopencv-3.4.2-h20b85fd_0\Library\etc\haarcascades\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame = cap.read()
    img = cv2.flip(frame,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(40, 40))

    for (x, y, w, h) in faces:
        gray_face = gray[(y):(y + h), (x):(x + w)]
        gray_face = cv2.resize(gray_face, (48, 48))
        gray_face = gray_face / 255.0
        gray_face = np.expand_dims(gray_face, 0)
        gray_face = np.expand_dims(gray_face, -1)
        emotion_label_arg = np.argmax(emotion_classifier.predict(gray_face))
        emotion = emotion_labels[emotion_label_arg]
        cv2.rectangle(img, (x + 10, y + 10), (x + h - 10, y + w - 10),
                      (255, 255, 255), 2)
        img = cv2.putText(img,emotion,(x+20,y+20),cv2.FONT_HERSHEY_DUPLEX,1.0,255,3)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xff ==27:
        break
cap.release()
cv2.destroyAllWindows()
