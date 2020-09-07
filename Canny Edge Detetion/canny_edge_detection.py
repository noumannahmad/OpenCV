# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 23:54:31 2020

@author: Nouman Ahmad
"""

import cv2

def nothing(x):
    pass

img = cv2.imread('houses.jpg',0)

# create trackbar for canny edge detection threshold changes

cv2.namedWindow('canny')

# add ON/OFF switch to canny

switch ='0 : OFF \n1 : ON'

cv2.createTrackbar(switch,'canny',0,1,nothing)

# add lower and upper threshold slidebars to canny


cv2.createTrackbar('lower','canny',0,255,nothing)
cv2.createTrackbar('upper','canny',0,255,nothing) 
 
while(True):
    
    # get current positions of 4 trackbars
    
    lower = cv2.getTrackbarPos('lower','canny')
    upper = cv2.getTrackbarPos('upper','canny')
    
    s = cv2.getTrackbarPos(switch,'canny')
    
    if s== 0:
        edges = img
        
       
    else:
        
        edges= cv2.Canny(img,lower,upper)
       
       
       # display images
       
    cv2.imshow('Orignal',img)
       
    cv2.imshow('canny',edges)
       
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
       
cv2.ddestroyAllWindows()        

