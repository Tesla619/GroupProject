from email.mime import image
import cv2, time, os, tensorflow as tf
import numpy as np

from tensorflow.python.keras.utils.data_utils import get_file

np.random.seed(20)

def showCamera():
    cap = cv2.VideoCapture(0)

    if (cap.isOpened() == False):
        print("Error opening file...")
        return

    (success, image) = cap.read()

    startTime = 0

    while success:
        currentTime = time.time()

        fps = 1/(currentTime - startTime)
        startTime = currentTime        

        cv2.putText(image, "FPS: " + str(int(fps)), (20, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0),2)
        cv2.imshow("Results", image)

        key = cv2.waitKey(1) & 0XFF
        if key == ord("q"):
            break

        (success, image) = cap.read()
    cv2.destroyAllWindows()
    
showCamera()