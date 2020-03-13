一、face_and_eye.py:

1.检测效果一般，经常检测为多个眼睛，靠近摄像头效果比较好

2.经常把鼻孔检测为眼睛，把感兴趣区域的高度设为脸部的一半可以有效解决，还有一点就是不要把你的鼻孔对准摄像头也能有效解决

使用文件：haarcascade_frontalface_default.xml、haarcascade_eye.xml



二、gender_classifier.py:

1.容易卡死，目前为止没有找到解决方法

使用文件：haarcascade_frontalface_default.xml、simple_CNN.81-0.96.hdf5



三、face_recognition.py

1.速度比较慢，明显卡顿



四、emotion.py

使用文件：simple_CNN.530-0.65.hdf5
