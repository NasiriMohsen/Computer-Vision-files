import cv2 as cv
import dlib 
import imutils
import numpy as np
from imutils import face_utils

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("/home/mohsencactus/Opencv/digit/opencv7_material/shape_predictor_68_face_landmarks.dat")

webcam = cv.VideoCapture(0)

while True:
    frame = webcam.read()[1]
    blank = np.zeros_like(frame)
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    rects = detector(gray,1)

    for rect in rects:
        (x1,y1) = (rect.left(),rect.top())
        (x2,y2) = (rect.right(),rect.bottom())
        #cv.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)

        shape = predictor(gray,rect)
        shape = face_utils.shape_to_np(shape)

        xa,ya = np.mean(shape,axis=0)
        xa,ya = int(xa),int(ya)

        for (x,y) in shape:
            cv.circle(frame,(x,y),3,(255,0,0),-1)
            cv.circle(blank,(x,y),3,(255,255,255),-1)
            cv.line(frame,(xa,ya),(x,y),(255,255,0),1)
                        
        cv.circle(frame,(xa,ya),3,(255,0,255),-1)

    cv.imshow("blank",blank)
    cv.imshow("frame",frame)
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break
    