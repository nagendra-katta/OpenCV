# import and show Webcam
import cv2

cap = cv2.VideoCapture(0)     # 0, 1  or 2 if more cameras are available, 0 for inbuilt camera
cap.set(3,640)   # width ID:3
cap.set(4,480)   # Height ID:4
cap.set(10,100)  # Brightness ID:10

while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break