import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    #roi = frame[269: 400, 537: 800] #top:bottom, left:right
    roi = frame[0: 1200, 0: 1200] #top:bottom, left:right
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    _, threshold = cv2.threshold(gray_roi, 100, 255, cv2.THRESH_BINARY_INV)
    #_, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #print(contours)

    cv2.imshow("Threshold", threshold)
    cv2.imshow("gray roi", gray_roi)
    cv2.imshow("Roi", roi)
    key = cv2.waitKey(30)
    if key == 27:
        break

cv2.destroyAllWindows()