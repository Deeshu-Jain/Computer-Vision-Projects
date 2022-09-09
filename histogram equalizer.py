import numpy as np
import cv2
import matplotlib.pyplot as plt

def img_read():
    while True:
        path=input("Enter the image's path(full path): ")
        pic = cv2.imread(path)
        if pic is None:
            print("Wrong file path entered")
            continue
        else:
            return pic
            break
 
def hist_eq(img):
    pic=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hsv[:,:,2]=cv2.equalizeHist(hsv[:,:,2])
    result=cv2.cvtColor(hsv,cv2.COLOR_HSV2RGB) 
    plt.subplot(121)
    plt.imshow(pic)
    plt.title("Original")
    plt.subplot(122)
    plt.imshow(result)
    plt.title("New")

    plt.show()

print("Histogram Equalizer")
IMG = img_read()
hist_eq(IMG)
