# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 22:15:19 2020

@author: Nouman Ahmad
"""

# Import libraries

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('img2.jpg',0)

# Extact Sobel Edges

#---------------------its emphasis Horizontal & vertical edges using sobel filter


sobel_x = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5) 
sobel_y = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)

cv2.imshow('Original image',image) 
cv2.waitKey(0)


cv2.imshow('sobel_x',sobel_x) #Horizontal
cv2.waitKey(0)


cv2.imshow('sobel_y',sobel_y) #Vertical
cv2.waitKey(0)

sobel_OR =cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow('sobel_OR',sobel_OR) #both combine
cv2.waitKey(0)
# Get Orientation
#-----------------------Gets all orientation-lengh & breath

laplacian = cv2.Laplacian(image,cv2.CV_64F)
cv2.imshow('laplacian',laplacian) #laplacian
cv2.waitKey(0)

# Apply Thresholds
#--------------------------------------applies thresholds i.e if a pixel is within upper and lower,threashold its concidered as an edge

canny = cv2.Canny(image,50,120)
cv2.imshow('canny',canny) #laplacian
cv2.waitKey(0)
# To display all images in console

plt.subplot(2,3,1),plt.imshow(image,cmap='gray')
plt.title('Original'),plt.xticks([]),plt.yticks([])

plt.subplot(2,3,2),plt.imshow(sobel_y,cmap='gray')
plt.title('sobel_x'),plt.xticks([]),plt.yticks([])

plt.subplot(2,3,3),plt.imshow(sobel_y,cmap='gray')
plt.title('sobel_y'),plt.xticks([]),plt.yticks([])


plt.subplot(2,3,4),plt.imshow(sobel_OR,cmap='gray')
plt.title('sobel_OR'),plt.xticks([]),plt.yticks([])

plt.subplot(2,3,5),plt.imshow(laplacian,cmap='gray')
plt.title('laplacian'),plt.xticks([]),plt.yticks([])
plt.show()