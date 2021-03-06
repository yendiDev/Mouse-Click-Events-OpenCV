"""
Project by Clinton Anani
This project demonstrates how to handle
mouse click events in OpenCV

github: yendiDev
email: kceequan01@gmail.com
"""

import cv2
import numpy as np


# print out all events
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_FLAG_LBUTTON:
        # left button clicked down
        print(x, ' ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        string_val = 'X:' + str(x) + ', Y: ' + str(y)
        # cv2.putText(img, string_val, (x, y), font, 1, (255, 255, 0), thickness=2)
        cv2.circle(img, (x, y), 10, color=(255, 255, 255), thickness=-1)
        cv2.imshow('image', img)


# create black image using numpy
img = np.zeros([512, 512, 3], np.uint8)

cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
