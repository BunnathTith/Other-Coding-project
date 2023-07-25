import cv2
import numpy as np
from PIL import Image

def get_limits(color):
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 10, 100, 110 #the lower bound and upperbound should be adjust acordingly depending on the background
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit


yellow = [255, 0, 255]
cap = cv2.VideoCapture(2)

while True:
    ret, frame = cap.read()
    imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower, upper = get_limits(yellow)
    mask = cv2.inRange(imgHSV, lower, upper)

    refine = cv2.GaussianBlur(mask, (3,3), 0)

    mask_ = Image.fromarray(refine)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame',frame)
    cv2.imshow('refine', refine)
    cv2.imshow('mask',mask)
    

    if cv2.waitKey(1) & 0xFF == ord('f'):
        break

cap.release
cv2.destroyAllWindows()
