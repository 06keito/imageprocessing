import cv2

def SHOWFPS(capture,frame,delay):
    fps = capture.get(cv2.CAP_PROP_POS_FRAMES)
    cv2.putText(frame,'nowFrame: {:.2f}'.format(fps),
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv2.putText(frame,'FPS: {:.2f}'.format(delay),
                (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), thickness=2)