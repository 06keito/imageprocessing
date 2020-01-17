def fillwhite_percent(img):#パーセントの画像変換　多分これいらない

    import cv2
    import numpy as np

    newimage = np.full((80,160,3), (255,255,255), dtype='uint8')
    newimage[10:70,60:100] = img

    return newimage

def fillwhite_Player(img):

    import cv2
    import numpy as np

    newimage = np.full((80,160,3), (255,255,255), dtype='uint8')
    newimage[10:70,0:160] = img

    return newimage