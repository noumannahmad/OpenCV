# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 13:49:42 2021

@author: Nouman ahmad
"""
import cv2
import numpy as np

img =cv2.imread('photo.png')

print(img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray =cv2.medianBlur(gray,5)
edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)

color=cv2.bilateralFilter(img,9,250,250)
cartoon=cv2.bitwise_and(color,color,mask=edges)

cv2.imwrite('result.png',cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
