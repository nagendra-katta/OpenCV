# Joining Images
'''
It is useful when we have lot of images and you are running it again and again, So its hard to manage to all these windows
together, So we will put all the images together in one windows
'''


import cv2
import numpy as np

img = cv2.imread("resources/ny_image.jpg")

# Horizontal stack (these are Numpy function not OPENCV)
"""
We have few problems here :
1. We cant resize the Image it will come as it is. If i add more images it will go out of the frame.
2. It should be same channels otherwise cant work. Example BGR BGR will work, BGR, GRAY not works.
    So both of them have to have same number of channels. Because theses are matrix
Solution: Prepared own function
 
"""
imgHor = np.hstack((img,img))

# Vertical stack
imgVer = np.vstack((img,img))


cv2.imshow("Out_Put",imgHor)
cv2.imshow("Out_Put2",imgVer)

# # Need to get solution from OPENCV Website
# imgSolh = stackImages(0.5, ([img,img,img]))
# imgSolhv = stackImages(0.5, ([img,img,img],[img,img,img]))



cv2.waitKey(0)