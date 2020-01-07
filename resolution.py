import cv2

read_path = "pictures/100%.jpg"

img = cv2.imread(read_path)
cut = cv2.imread(read_path)

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

#Player_A = img[560:720, 320:480]
Player_B = img[610:670, 858:898]

#cv2.imshow("cut",cut)
#cv2.imshow("Player_A",Player_A)
cv2.imshow("Player_B",Player_B)

#cv2.imwrite("pictures/Player_A.jpg",Player_A)
cv2.imwrite("pictures/tmp/0_percent.jpg",Player_B)

cv2.waitKey(0)
cv2.destroyAllWindows()