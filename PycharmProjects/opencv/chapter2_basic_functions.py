# Basic_functions

import cv2
import numpy as np

# Original image
img = cv2.imread("resources/ny_image.jpg")



# Gray Image
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # In Open CV RGB is called as BGR

# Blur Image
imgBlur = cv2.GaussianBlur (imgGray,(7,7), 0)  # ksize should be odd number example(7,7) or (3,3)

# Canny Image Finding edges
imgCanny = cv2.Canny(imgGray,100,100)   # we call it as canny edge detector

# Dilation
"""
Sometimes we are detecting an edge but because there is a gap or because its not joined it does not detect it as a proper line.
So we can increase the thickness of our edge.
We need to difine matrix for dilate so we are using Numpy to deal with matrix
"""
# kernel is a matrix we have define the size of and the value of which have all one values
# uint8 means unsigned int 8 means the valuesfrom 0 to 255
kernel = np.ones((5,5),np.uint8)
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1) # iterations means how mach thick


# Erode -> opposite to dilation (thinning the line)
imgEroded = cv2.erode(imgDilation,kernel,iterations=1)




cv2.imshow("Original Image",img)
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("dilation Image",imgDilation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)