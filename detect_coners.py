# -*- coding: utf-8 -*

import cv2

path = "C:/Users/keito/picture/SSBU_PERCENT/resize8080.jpg"

try:
    MAX_CORNERS = 50
    BLOCK_SIZE = 3
    QUALITY_LEVEL = 0.01
    MIN_DISTANCE = 20.0

    img = cv2.imread(path)

    if img is None:
        print ('ファイルを読み込めません。')
        import sys
        sys.exit()

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, MAX_CORNERS, QUALITY_LEVEL, MIN_DISTANCE,
                                      blockSize = BLOCK_SIZE, useHarrisDetector = False)

    for i in corners:
        x,y = i.ravel()
        cv2.circle(img, (x,y), 4, (255, 255, 0), 2)

    #cv2.imwrite('c:/temp/corners.jpg', img)
    cv2.imshow('img', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))