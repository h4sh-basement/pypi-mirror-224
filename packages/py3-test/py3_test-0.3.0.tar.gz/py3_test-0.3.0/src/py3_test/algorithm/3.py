"""
@author: lijc210@163.com
@file: 2.py
@time: 2020/07/20
@desc: 功能描述。
"""

import cv2
import numpy as np

path = "result.jpg"  # 记得不要有中文路径

img = cv2.imread(path)
height, width = img.shape[0:2]
# 开始操作
# thresh = cv2.inRange( img,np.array([128,138,135]),np.array([192,192,192]) )
thresh = cv2.inRange(img, np.array([0, 0, 0]), np.array([192, 192, 192]))
scan = np.ones((3, 3), np.uint8)
cor = cv2.dilate(thresh, scan, iterations=1)
specular = cv2.inpaint(img, cor, 5, flags=cv2.INPAINT_TELEA)
# 操作结束，下面开始是输出图片的代码
cv2.namedWindow("image", 0)
cv2.resizeWindow("image", int(width / 2), int(height / 2))
cv2.imshow("image", img)

cv2.namedWindow("modified", 0)
cv2.resizeWindow("modified", int(width / 2), int(height / 2))
cv2.imshow("modified", specular)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("result2.jpg", specular)
