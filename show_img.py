import cv2

img = cv2.imread('00-puppy.jpg')

while True:
    cv2.imshow('Pupppy',img)

    # if we've waited at least 1ms and we've pressed the ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()