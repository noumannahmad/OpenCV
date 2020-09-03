# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 10:46:55 2020

@author: Nouman Ahmad
"""
#OpenCV Python prgoram to detect cars in video frame


# import libraries of python openCv

import cv2

# capture frame from a video

cap = cv2.VideoCapture('cars.mp4')

#Trained XML classifiers describes some features of some objets we want to detect

car_cascade = cv2.CascadeClassifier('cars.xml')

#Loop runs if capturing has been initialized.

while True:
     #reads frames from a video
     
     ret , frames = cap.read()
     #convert to gray scale of each frames
     gray = cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
     #Detect cars of different size in the imput image
     cars = car_cascade.detectMultiScale(gray,1.1,1)
     # To draw a rectangle in each cars
     for (x,y,w,h) in cars:
         cv2.rectangle(frames,(x,y),(x+w,y+h),(0,225,0),2)
         # display frames in a window
         cv2.imshow('Car Detection',frames)
       #Wait for enter key to stop
     if cv2.waitKey(33)== 13:
         break
cv2.destroyAllWindows()     
         