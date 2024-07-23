# Colour Detection
"""
Task is detecting the orange colour in image.
1. Need to convert into HSV space
2. Create a Trackbar to get Colour values
3. Now we need to define some colour values some ranges in which we want our colour to be.
   So we will define the hue, saturation and the value limits and with in that limit.
   If the image region falls with in that colour range we will grab that.
   (But one thing to note that we do not actually know what is the min and max values
   are that we need for this particular orange colour). So we are going to introduce track
   bars that will help us play around with the values in real time so that we can find optimum min and max values.
4. (MASK)Now using these values we need to filter out our image so that we can get our particular colour of the image
    Using the mask we need to filter out that colour that we don't need using Trackbar adjustments
    (black means  0,s not required, white means 1's required)
5. Now update the initial(min) values in Trackbars
6. Now we can get our Result which will be our original colour (Orange) by creating a new image using mask
"""


import cv2
import numpy as np

def empty(a):
    pass

path = "resources/ny_image.jpg"

# 2. Creating Trackbars (it required dummy function so added empty())
# The Trackbar name should be same in all windows
cv2.namedWindow("Trackbars") # Trackbar Name
cv2.resizeWindow("Trackbars",640,240)       # Trackbar size
# Total 6 Trackbars for 6 values
# In general max value of hue is 360 but in Ope ncv Hue max is 180(0-179)
# At the end we have to call a function which will run every time something changes in trackbar(Otherway we will check later)
cv2.createTrackbar("Hue Min", "Trackbars",0,179,empty)
cv2.createTrackbar("Hue Max", "Trackbars",12,179,empty)
cv2.createTrackbar("Sat Min", "Trackbars",73,255,empty)
cv2.createTrackbar("Sat Max", "Trackbars",255,255,empty)
cv2.createTrackbar("Val Min", "Trackbars",122,255,empty)
cv2.createTrackbar("Val Max", "Trackbars",255,255,empty)

# 1. Create HSV Image
img = cv2.imread(path)
imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# 3. Get track bar values (colour values)
while True:
    h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")
    print (h_min, h_max, s_min, s_max, v_min, v_max)

    # 4. mask
    lower = np.array([h_min, s_min,v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imghsv,lower,upper)

    # 6.
    # Bitwise AND will add two images together to create a new image
    # It will compare both images when both pixels present it will take
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("Original",  img)
    cv2.imshow("HSV_Output",  imghsv)
    cv2.imshow("MASK", mask)
    cv2.imshow("Result", imgResult)
    cv2.waitKey(1)