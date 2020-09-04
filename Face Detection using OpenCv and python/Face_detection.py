# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 16:04:18 2020

@author: Nouman Ahmad
"""

# Install ------------- pip install opencv-python


import cv2

# load cascade 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 
# Read the input image

img = cv2.imread('image1.jpg')

# convert into grayscale

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Detect faces

faces = face_cascade.detectMultiScale(gray,1.1,4)

#Draw rectangle around the faces

for (x,y,w,h) in faces:
    
    cv2.rectangle(img,(x,y),(x+w,y+h),(225,225,156),2)
    
#display the output

cv2.imshow('image',img)
cv2.waitKey()    