#画像の二値化

import cv2

read_path = ""
save_path = ""

try:
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    threshold = 60 #閾値の設定

    if img is None:
        print ('ファイルを読み込めません。')
        import sys
        sys.exit()

    ret, img_thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    cv2.imwrite(save_path, img_thresh)

    cv2.imshow('img', img_thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))