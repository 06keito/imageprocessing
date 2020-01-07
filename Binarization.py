# -*- coding: utf-8 -*

import cv2

path = "pictures/tmp/9_percent.jpg"

try:
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print ('ファイルを読み込めません。')
        import sys
        sys.exit()
    threshold = 60
    ret, img_thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    print("ret: {}".format(ret))
    cv2.imwrite('pictures/tmp/Binarization/Binarization_9_percent.jpg', img_thresh)

    cv2.imshow('img', img_thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))