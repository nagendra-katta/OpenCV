# Resize and cropping

import cv2
import numpy as np

# Original image
img = cv2.imread("resources/ny_image.jpg")
print(img.shape)  # Displays (Height, Width, Channels)

imgResize = cv2.resize(img,(1000,500))   # width came first here Width= 1000 Height = 500
print(imgResize.shape)

# for crop no need cv2 function we can directly use Matrix from starting point
imgCrop = img[0:200,200:500] # the tricky point is here height comes first


print(imgCrop.shape)

cv2.imshow("Original Image",img)
cv2.imshow("imgResize",imgResize)
cv2.imshow("imgCrop",imgCrop)

cv2.waitKey(0)