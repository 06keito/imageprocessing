import cv2
import numpy as np
import sys

Path_Movie_File = "hoge"#読み込むファイル
Path_Save_File = "hoge"#保存するファイル
delay = 1
window_name = "hoge"#window表示時の名前

capture = cv2.VideoCapture(Path_Movie_File)

if not capture.isOpened():#ファイルが存在しない場合
    sys.exit()

try:
    while(1):
        ret, frame = capture.read()#フレームの画像が読み込めたかどうかを示すbool値と画像の配列ndarrayのタプル
        if ret:
            cv2.imshow(window_name,frame)
            if cv2.waitKey(delay)&0xff==ord("q"):#終了キー
                break
    cv2.destroyAllWindows(window_name)

except:#エラー処理
    print("Error:",sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))