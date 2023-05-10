import cv2
import numpy as np

#################
##  VARIABLES  ##
#################
img = np.zeros((512,512,3))
xy_orig = (0,0)
drawobj = False
orig = np.copy(img)
 
# Funcs
def draw_rectangle(event, x, y, flags, params):
    global xy_orig, drawobj, orig, img, last_xy
    if event == cv2.EVENT_LBUTTONDOWN:
        xy_orig = (x,y)
        drawobj = True
        orig    = np.copy(img)
    elif (event == cv2.EVENT_MOUSEMOVE) and (drawobj == True):
        img = np.copy(orig)
        cv2.rectangle(img, pt1=xy_orig, pt2=(x,y), color=(255,255,255), thickness=1)
        last_xy = (x,y)
    elif event == cv2.EVENT_LBUTTONUP:
        img = np.copy(orig)
        cv2.rectangle(img, pt1=xy_orig, pt2=(x,y), color=(255,255,255), thickness=3)
        drawobj = False


cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing',draw_rectangle)

while True:

    cv2.imshow('my_drawing',img)

    # check for hitting esc key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
