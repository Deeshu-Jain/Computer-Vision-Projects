import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

face_cascade = cv2.CascadeClassifier("data/haarcascade/haarcascade_frontalface_default.xml")

def detect_face(img):
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    new_img = img.copy()
    face_rects = face_cascade.detectMultiScale(img_gray,scaleFactor=1.2,minNeighbors=5)
    for (x,y,w,h) in face_rects:
        cv2.rectangle(new_img,(x,y),(x+w,y+h),(255,255,255),10)
    return new_img

def web_cam():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        frame = detect_face(frame)
        cv2.imshow("Video Face Detection",frame)
        k=cv2.waitKey(1)
        if k==27:
            break
        
    cap.release()
    cv2.destroyAllWindows()

def img_read():
    while True:
        path=input("Enter the image's path(full path): ")
        pic = cv2.imread(path)
        if pic is None:
            print("Wrong file path entered")
            continue
        else:  
            Photo=cv2.resize(pic.copy(),(800,600))
            result = detect_face(Photo)
            cv2.imshow("result",result)
            if cv2.waitKey(1) & 0xFF==27 :
                break
    cv2.destroyAllWindows()

def vid_read():
    while True:
        path=input("Enter the video's path/location: ")
        cap = cv2.VideoCapture(path)
        if cap.isOpened() == False:
            print("Wrong file path entered")
            continue   
        else:
            break
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    while cap.isOpened():
        ret,frame = cap.read()
        if ret == True:
            #time.sleep(1/(fps))
            #no need for applying this becoz haarcascades detection already make it slow
            frame = detect_face(frame)
            cv2.imshow("frame",frame)
            if cv2.waitKey(10) & 0xFF == 27:
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

def number_input():
    while True:
        try:
            n = int(input("Enter your choice (1-3) "))
            if n in range(1,4):
                return n
            else:
                print("Invalid Choice! Try Again")
        except:
            print("Invalid Choice! Try Again")



#-------------DETECT FACES APPLICATION-------------
print("------------------DETECT FACES APPLICATION------------------")
print("{In case of Using WebCam or playing Video press Esc to EXIT}")
print("\n1. Detecting front face using webcam")
print("2. Detecting front face in an image")
print("3. Detetcing front face in a video(Not Quite Good Working)\n")
choice = number_input()
if choice==1:
    web_cam()
elif choice==2:
    img_read()
else: #choice==3
    vid_read()