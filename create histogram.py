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
 
def create_hist(img): 
    color = ( 'b' , 'g' , 'r' )
    for i,col in enumerate(color):
        result=cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(result,color=col)
        plt.xlim([0,256])
    plt.title("Histogram")
    plt.show()

IMG = img_read()
create_hist(IMG)
