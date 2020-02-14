import cv2 as cv
import os
import time

# 获取视频
cap = cv.VideoCapture(0)

#获取视频帧数
fps =cap.get(cv.CAP_PROP_FPS)
# 获取视频宽度
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
# 获取视频高度
height= cap.get(cv.CAP_PROP_FRAME_HEIGHT)

# 保存图片10张

# 图片个数
i = 0

# 根据当前时间，创建图片文件夹
base_name = str(time.time())
os.mkdir(base_name)

# 摄像头是否打开
while cap.isOpened():
    if i == 50:     #10张图片就退出
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
    time.sleep(0.1)

print('\n{}张图片保存完成'.format(i))

# 视频合成
# shape = (width,height)
# fourcc = cv.VideoWriter_fourcc(*'XVID')   # 1. *'MP4V' => .mp4  2. *'XVID' => .avi
# video_write = cv.VideoWriter('a.avi',fourcc,10,(int(width),int(height)))  # 1.保存文件名  2.编码器  3.每秒帧数  4.视频尺寸
# for i in range(1,51):
#     img = cv.imread(base_name+'/frame'+str(i)+'.jpg')
#     video_write.write(img)
# print('视频已经合成')

