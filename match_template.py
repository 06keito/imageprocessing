#テンプレートマッチング
import cv2

path_A = "background.jpg"
path_B = "1.jpg"

try:
    img = cv2.imread(path_A)
    templ = cv2.imread(path_B)

    if img is None or templ is None:
        print ('ファイルを読み込めません。')
        import sys
        sys.exit()

    result = cv2.matchTemplate(img, templ, cv2.TM_CCOEFF_NORMED)
    mmr = cv2.minMaxLoc(result)
    pos = mmr[3]

    dst = img.copy()
    cv2.rectangle(dst, pos, (pos[0] + templ.shape[1], pos[1] + templ.shape[0]),
                  (0, 0, 255), 2)

    #cv2.imwrite('c:/temp/dst_match.jpg', dst)
    cv2.imshow('dst', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))