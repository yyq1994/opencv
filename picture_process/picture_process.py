import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# # 随机创造图片
# sjpicture = np.zeros([200,200,3],np.uint8)
# sjpicture[:,:,0] = np.random.randint(0,256)
# sjpicture[:,:,1] = np.random.randint(0,256)
# sjpicture[:,:,2] = np.random.randint(0,256)
# cv.imshow('随机图片',sjpicture)
# cv.waitKey(0)
# 加载图片
img = cv.imread('img/a2.jpg',1)

# 图片信息（高、宽、通道）
img_info = img.shape

# 图片缩放
dst = cv.resize(img,(int(img_info[1]*0.5),int(img_info[0]*0.5)))
cv.imshow('resize',dst)
cv.waitKey(0)

# # 图片位移
# matshift = np.float32([[1,0,100],[0,1,200]])
# move = cv.warpAffine(img,matshift,(img_info[1],img_info[0]))  #第三个参数对应图片的宽高（x轴Y轴）
# cv.imshow('move',move)
# cv.waitKey(0)

# 放射变换   (img左上、左下，右上 =>
#            dst左上、左下，右上)
# pts1 = np.float32([[0,0],[200,0],[0,200]])
# pts2 = np.float32([[10,10],[150,50],[50,150]])
#
# M = cv.getAffineTransform(pts1,pts2)
# fs = cv.warpAffine(img,M,(img_info[1],img_info[0]))
# cv.imshow('fs',fs)
# cv.waitKey(0)

# # 旋转
# M = cv.getRotationMatrix2D((img_info[1]/2,img_info[0]/2),20,0.5)  #旋转中心，旋转角度，图片缩放
# rotate = cv.warpAffine(img,M,(img_info[1],img_info[0]))
# cv.imshow('rotate',rotate)
# cv.waitKey(0)


# # 灰度处理
# # 方法一
# # gray = cv.imread('img/a2.jpg',0)
# # cv.imshow('gray',gray)
# #方法二
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
# cv.imshow('gray',gray)

# # 颜色反转 负片
# fp = 255-img
# cv.imshow('fp',fp)

# # 图片融合
# img2 = cv.imread('img/a.jpg')
# img2 = cv.resize(img2,(img_info[1],img_info[0]))
# rh = cv.addWeighted(img,0.3,img2,0.7,0)
# cv.imshow('rh',rh)

## 边缘检测
# imgG = cv.GaussianBlur(gray,(5,5),0)
# byjc = cv.Canny(imgG,120,250)
# cv.imshow('img,',byjc)

# # 直线
# cv.line(img,(50,550),(500,600),(0,0,255),thickness=20,lineType=cv.LINE_8)   #1.图片 2.起始位置  3.终止位置  4.颜色  5.线宽
# cv.line(img,(50,550),(40,600),(0,0,255),thickness=20,lineType=cv.LINE_AA)

# 矩形
# cv.rectangle(img,(50,50),(600,600),(200,50,200),-1)  #线宽设为-1.实心矩形

# 圆形
# cv.circle(img,(500,500),200,(255,255,0),10)

# 椭圆
# cv.ellipse(img,(600,400),(200,150),10,0,270,(0,255,255),10) #3.轴的长度

# 多边形
# point = np.array([[100,100],[100,200],[50,300],[400,50],[600,500],[100,100]],np.int32)
# point = point.reshape((-1,1,2))
# cv.polylines(img,[point],True,(200,200,100),10)

# 文字
# font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
# cv.putText(img,'I love you so much',(300,300),font,4,(0,200,190),5,cv.LINE_AA)  # 3. 写入坐标  5.字体大小

# # 直方图
# color = ['b','g','r']
# for num,col in enumerate(color):
#     hist = cv.calcHist([img],[num],None,[256],[0,256])
#     plt.plot(hist,color=color[num])
#     plt.xlim([0,256])
# plt.show()

# 直方图均衡化
# 彩色
# b,g,r = cv.split(img)
# b = cv.equalizeHist(b)
# g = cv.equalizeHist(g)
# r = cv.equalizeHist(r)
# qh = cv.merge((b,g,r))
# cv.imshow('equalize',qh)

# 双边滤波
# doubleBlur = cv.bilateralFilter(img,15,35,35)
# cv.imshow('double',doubleBlur)

# 高斯滤波
# gs = cv.GaussianBlur(img,(3,3),0)
# cv.imshow('GaussianBlur',gs)

# 中值滤波
# medianBlur = cv.medianBlur(img,3)
# cv.imshow('medianBlur',medianBlur)
# cv.waitKey(0)
