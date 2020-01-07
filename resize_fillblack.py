def fillblack(img):

    import cv2
    import numpy as np

    newimage = np.zeros((60,160,3),np.uint8)
    newimage[:,:] = [255,255,255]
    cv2.rectangle(img, (0, 0), (40, 160), (255, 255, 0))
    newimage[0:60,60:100] = img

    return newimage