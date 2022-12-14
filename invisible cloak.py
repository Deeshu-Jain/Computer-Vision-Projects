import cv2
import numpy as np
import time

video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
time.sleep(3)
for i in range(60):
    check,bg = video.read()
bg=np.flip(bg,1)
while True:
    check,img=video.read()
    if check == False:
        break
    img=np.flip(img,1)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    

    # ranges should be carefully chosen
    # setting the lower and upper range for mask1
    lower_red = np.array([100, 40, 40])       
    upper_red = np.array([100, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    # setting the lower and upper range for mask2 
    lower_red = np.array([155, 40, 40])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    mask1= mask1+mask2
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))
    mask2=cv2.bitwise_not(mask1)
    res1=cv2.bitwise_and(img,img,mask=mask2)
    res2=cv2.bitwise_and(bg,bg,mask=mask1)

    final=cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow("final",final)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()


