import cv2
import numpy as np
import dlib

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        #cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

        landmarks = predictor(gray, face)
        x = landmarks.part(36).x
        y = landmarks.part(36).y
        cv2.circle(frame, (x, y), 3, (0, 0, 255), 2)
        #print(face)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()