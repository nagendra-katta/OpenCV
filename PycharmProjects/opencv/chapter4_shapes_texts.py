# Shapes and texts

import cv2
import numpy as np


# img = np.zeros((512,512))  # zeros means black, 513 sidth, 512 height, grayscale


# Creating black colour image with pixels 512,512
img = np.zeros((512,512,3),np.uint8) # zeros means black, 513 sidth, 512 height, 3 layers(BGR)
print(img.shape)  # to print the size(pixels) of image

# change blue colour to image
img[:] = 255,0,0  # img[:] in braces colon like crop starting and ending of the pixels, check below example
# Only [:] whole image
# img[200:300,100:300] = 255,0,0 # 1st is height from 200 pixel to 300 pixel and width 100 to 300 change to blue colour

# Line function
# Params are img src, starting point, ending point, colour(we used green), line thickness
# cv2.line(img,(0,0),(300,300),(0,255,0),3)

# Line from start to end
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)


# Create a Rectangle
cv2.rectangle(img, (0,0),(250,350),(0,0,255),3)  # Params same as line


# Filled Rectangle
# cv2.rectangle(img, (0,0),(250,350),(0,0,255),cv2.FILLED) # instead of thickness used cv2.FILLED to fill colour


# Create Circle
# Params are img src, center width and height, radius of circle, colour, thickness
cv2.circle(img, (400,300),30, (255,255,0),5)


#  Text on Image
# Params : img src, Text, Origin:where we need to pu text, font, scale(font size), colour, thickness(line thicknell)
cv2.putText(img, " OPENCV ", (300,100),cv2.FONT_HERSHEY_COMPLEX,1, (0,150,0),3)



cv2.imshow("Image",img)
cv2.waitKey(0)