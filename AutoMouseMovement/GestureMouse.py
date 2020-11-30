import cv2
import numpy as np
import pyautogui

video = cv2.VideoCapture(0)
while True:
    ret, frame = video.read()
    cv2.imwrite("frame.jpg", frame)
    cv2.resize(frame, (1280, 720))
    img = cv2.imread("cursor_right.jpg")

    diff = cv2.subtract(frame, img)
    print(diff)

    cv2.imshow("Hand", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
