import cv2
import glob
import numpy as np
import os
import resize_fillblack


moviepath = "pictures/testimage.jpg"#プレイ画面の映像または写真を取得
percentpath = "pictures/percent/Binarization_percent/Binarization_1_percent.jpg"
#glob.glob("pictures/percent/Binarization_percent/*")#パーセントのテンプレート用の写真のパスを取得

threshold = 100 #閾値の設定

img = cv2.imread(moviepath,0)#第二引数に0を書き込むことでグレースケールにする
percent = cv2.imread(percentpath)

ret, img_thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)#二値化

Player_A = img_thresh[610:670, 320:480]#ポート番号1のプレイヤーの状態を取得
Player_B = img_thresh[610:670, 800:960]#ポート番号2のプレイヤーの状態

percent = resize_fillblack.fillblack(percent)#画像のサイズをそろえるための処理

SCALE = 1.5
percent = cv2.resize(percent,(int(percent.shape[1]*SCALE),int(percent.shape[0]*SCALE)))
Player_A = cv2.resize(Player_A,(int(Player_A.shape[1]*SCALE),int(Player_A.shape[0]*SCALE)))


detector = cv2.AKAZE_create()

kp1, des1 = detector.detectAndCompute(Player_A, None)
kp2, des2 = detector.detectAndCompute(percent, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING)

matches = bf.knnMatch(des1, des2, k=2)

ratio = 0.9
good = []
for m, n in matches:
    if m.distance < ratio * n.distance:
        good.append([m])


img3 = cv2.drawMatchesKnn(Player_A, kp1, percent, kp2, good, None, flags=2)

cv2.imshow("Player_A",Player_A)
cv2.imshow("Player_B",Player_B)
cv2.imshow("percent",percent)
cv2.imshow('img', img3)



cv2.waitKey(0)
cv2.destroyAllWindows()