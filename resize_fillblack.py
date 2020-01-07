def fillblack(img):

    import cv2
    import numpy as np

    newimage = np.zeros((60,160,3),np.uint8)
    newimage[:,:] = [255,255,255]
    cv2.rectangle(img, (0, 0), (160, 60), (255, 255, 0))
    newimage[60:120,0:40] = img

    return newimage