import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

kernel = np.ones((5,5),np.uint8)
img = cv2.imread("Birch Test 1/img-Color2.png")
orgimg = cv2.imread("Birch Test 1/img-Color2.png")
# images = []
# for filename in os.listdir("Birch Test 1"):
#     img = cv2.imread(os.path.join("Birch Test 1", filename))
#     if img is not None:
#         images.append(img)
#     print(img.shape)
# i = 0
# for img in images:

# Blur to remove particles
# img = cv2.bilateralFilter(img, 7,75,75)
# # Color alteration
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        (b, g, r) = img[x, y]
        if b > 250:
            img[x, y] = (b * 0.7, g * 1, r * 1.4)
        elif r>250:
            img[x, y] = (b*0.7, g, r)
        else:
            img[x, y] = (b * 0.9, g * 1, r * 1.2)
        if int(b) + int(g) + int(r) > 700:
            img[x, y] = (b, g, r)
    # cv2.imwrite(os.path.join("Birch Test 1 Results", str(i) + ".png"), img)
    # i += 1

resize_constant = 1

# Resizing to fit on my computer
width = int(img.shape[1] * resize_constant)
height = int(img.shape[0] * resize_constant)
dsize = (width, height)
resizeimg = cv2.resize(img, dsize)
cv2.imshow("modified", resizeimg)
width = int(orgimg.shape[1] * resize_constant)
height = int(orgimg.shape[0] * resize_constant)
dsize = (width, height)
resizeorgimg = cv2.resize(orgimg, dsize)
cv2.imshow("original", resizeorgimg)

# kelp identification
hsv = cv2.cvtColor(resizeimg,cv2.COLOR_BGR2HSV)

green_lower = np.array([50, 106, 92], np.uint8)
green_upper = np.array([102, 255, 255], np.uint8)

mask = cv2.inRange(hsv,green_lower, green_upper)
mask = cv2.bitwise_not(mask)
cv2.imshow("kelp removed", mask)
# opening and closing
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
res = cv2.bitwise_and(resizeimg,resizeimg,mask=mask)
cv2.imshow("kelp only", res)
cv2.imwrite(os.path.join("Birch Test 1 Results",  "pres.png"), res)
cv2.waitKey()
