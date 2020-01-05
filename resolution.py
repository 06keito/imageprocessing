import cv2

path = "hoge"
img = cv2.imread(path)
cut = cv2.imread(path)

height, width, channels = img.shape[:3]
print("width: " + str(width))
print("height: " + str(height))


square_size = 80

for i in range(0,height,square_size):
    for j in range(0,width,square_size):
        cv2.line(cut,(j,0),(j,height),(255,0,0))
        cv2.putText(cut,'({},{})'.format(j,i),
            (j,i+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), thickness=1)
    cv2.line(cut,(0,i),(width,i),(255,0,0))



#cut = img[0 : 500, 0: 500]

cv2.imshow("cut",cut)

cv2.waitKey(0)
cv2.destroyAllWindows()