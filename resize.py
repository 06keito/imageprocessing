#画像ファイルのリサイズ

import cv2

path = ""

try:
    img = cv2.imread(path)

    if img is None:
        print ('ファイルを読み込めません。')
        import sys
        sys.exit()

    SCALE1 = 1
    SCALE2 = 1
    height = img.shape[0]
    width = img.shape[1]

    dst = cv2.resize(img, dsize=(80,80))
    #dst = cv2.resize(img, (int(width*SCALE1), int(height*SCALE1)))
    #cv2.imwrite('', dst)
    cv2.imshow('dst1', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))