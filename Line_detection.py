# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 21:23:27 2020

@author: Nouman Ahmad
"""

import cv2
cap = cv2.VideoCapture('car_line.mp4')

while True:
    ret, img = cap.read()
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    canny = cv2.Canny(blur,10,70)
    ret, mask= cv2.threshold(canny,70,255,cv2.THRESH_BINARY)
    cv2.imshow('Video',mask)
    
    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()    