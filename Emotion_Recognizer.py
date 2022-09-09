#pip install tensorflow, fer, opencv-python
from fer import FER
import matplotlib.pyplot as plt 
import cv2
import numpy as np
def emotion_detection():
    #Using cv2.CAP_DSHOW removes the warning, but slows down my frame rate from 30fps to 7fps, on Windows.
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    while True:
        ret, frame = cap.read()
        emo_detector = FER(mtcnn=True)
        #frame = detect_face(frame)
        cv2.imshow("Emotion Recognition",frame)
        k=cv2.waitKey(1)
        if k==27:
            out = cv2.imwrite('capture.jpg', frame)
            dominant_emotion, emotion_score = emo_detector.top_emotion(frame)
            print(dominant_emotion, emotion_score)
            break
        
    cap.release()
    cv2.destroyAllWindows()

emotion_detection()