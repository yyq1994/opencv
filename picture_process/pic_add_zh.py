import numpy as np
import cv2 as cv
from PIL import ImageFont,ImageDraw,Image

# 1. 转为PIL图片格式
# 2. 用PIL绘制文字
# 3. 转为OpenCV图片格式

def draw_zh(img,text,left,top,color=(255,0,0),size=50):
    # 1. 转为PIL图片格式
    img = Image.fromarray(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    # 2. 用PIL绘制文字
    draw = ImageDraw.Draw(img)
    # 设置字体
    font = ImageFont.truetype('font/simsun.ttc',size,encoding='utf-8')
    draw.text((left,top),text,color,font)
    # 3. 转为OpenCV图片格式
    return cv.cvtColor(np.asarray(img),cv.COLOR_RGB2BGR)

img = cv.imread('img/a.jpg')
img = draw_zh(img,'爱你呦',200,200,size=100)
cv.imshow('aa',img)
cv.waitKey(0)