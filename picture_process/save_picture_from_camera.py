import time
import cv2 as cv
import os
import shutil
import time
cap = cv.VideoCapture(0)
# 保存图片10张

# 图片个数
i = 0

# 根据当前时间，创建图片文件夹
base_name = str(time.time())
os.mkdir(base_name)

# 摄像头是否打开
while cap.isOpened():
    if i == 10:     #10张图片就退出
        break
    else:
        i += 1

    # flag:是否读取成功
    flag,frame = cap.read()

    #设置图片名称
    file_name = base_name+'/frame'+str(i)+'.jpg'

    # 显示图片
    cv.imshow(file_name,frame)

    # 保存图片到文件夹,全质量保存
    cv.imwrite(file_name,frame,[cv.IMWRITE_JPEG_QUALITY,100])

    # 提示图片保存成功
    print('第{} 张图片保存成功'.format(i))

    # 每1秒保存一张图片
    time.sleep(1)


print('\n10张图片保存完成')
