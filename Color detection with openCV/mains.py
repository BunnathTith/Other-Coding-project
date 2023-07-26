import cv2
import numpy as np
from PIL import Image


cap = cv2.VideoCapture(2)

while True:
    ret, frame = cap.read()
    imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(imgHSV, (85, 100, 100), (95, 255, 255))
    # green = (45, 100, 100), (75, 255, 255)
    # yellow = (85, 100, 100), (95, 255, 255)
    refine = cv2.GaussianBlur(mask, (3,3), 0)

    mask_ = Image.fromarray(refine)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

    cv2.imshow('frame',frame)
    #cv2.imshow('refine', refine)
    cv2.imshow('mask',mask)
    

    if cv2.waitKey(1) & 0xFF == ord('f'):
        break

cap.release
cv2.destroyAllWindows()
