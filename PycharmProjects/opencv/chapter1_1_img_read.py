# import and display image


import cv2

# Attempt to read the image
img = cv2.imread("resources/ny_image.jpg")

# Check if the image was successfully loaded
if img is None:
    print("Error: Image not loaded. Check the file path.")
else:
    cv2.imshow("Output", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

