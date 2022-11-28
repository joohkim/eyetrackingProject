import cv2
import numpy as np

#cap = cv2.VideoCapture("20221126_002822.mp4")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    roi = frame[89: 169, 537: 800] #top:bottom, left:right
    #roi = frame[0: 1000, 0: 1000] #top:bottom, left:right
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)

    _, threshold = cv2.threshold(gray_roi, 50, 255, cv2.THRESH_BINARY_INV)

    cv2.imshow("Threshold", threshold)
    cv2.imshow("gray roi", gray_roi)
    cv2.imshow("Roi", roi)
    key = cv2.waitKey(30)
    if key == 27:
        break

cv2.destroyAllWindows()