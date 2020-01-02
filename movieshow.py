import cv2
import numpy as np
import sys
from function import ShowFPS

Path_Movie_File = "hoge.mp4"#読み込むファイル
Path_Save_File = "hoge"#保存するファイル
window_name = "frame"#window表示時の名前
capture = cv2.VideoCapture(Path_Movie_File)

if not capture.isOpened():#ファイルが存在しない場合
    sys.exit()

delay = int(capture.get(cv2.CAP_PROP_FPS)) #FPS値を取得,intである必要がある

try:
    while(1):
        ret, frame = capture.read()#フレームの画像が読み込めたかどうかを示すbool値と画像の配列ndarrayのタプル
        if ret:
            ShowFPS.SHOWFPS(capture,frame,delay)#現在のフレームを表示
            cv2.imshow(window_name,frame)
            if cv2.waitKey(delay)&0xff==ord("q"):#終了キー
                break
    cv2.destroyAllWindows(window_name)
    capture.release()

except:#エラー処理
    print("Error:",sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))