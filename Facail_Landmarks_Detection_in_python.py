# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 12:40:52 2020

@author: Nouman Ahmad
"""



# link for Face landmark models 

#https://github.com/davisking/dlib-models

import cv2
import dlib

cam= cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


while True:
    ret ,img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)
        for n in range(0,68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(img,(x,y),4,(0,255,0),-1)
    
    cv2.imshow("Frames",img)
    if (cv2.waitKey(1)==ord('q')):
            break
cam.release()
cv2.destroyAllWindows()
   