import numpy as npy
import cv2
import sys

MAX = 255

# Jika gambarnya GRAYSCALE
if(sys.argv[2]=="gray"):
    #Membaca Input dengan format "python negative.py "gambar.jpg" gray"
    img = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE) 
    gambar = npy.array([MAX-x for x in img])
    cv2.imwrite('negativegray.jpg', gambar)
    cv2.imshow('negativegray.jpg', gambar) 

# Jika gambarnya RGB
else:  
    #Membaca Input dengan format "python negative.py "gambar.jpg" rgb"
    img = cv2.imread(sys.argv[1],cv2.IMREAD_COLOR)    
    R,G,B = cv2.split(img)
    R[:] = [MAX-x for x in R]
    G[:] = [MAX-x for x in G]
    B[:] = [MAX-x for x in B]

    #SAVE
    gambar = cv2.merge((R, G, B)) 
    cv2.imwrite('negativergb.jpg', gambar)
    cv2.imshow('negativergb.jpg', gambar)  
