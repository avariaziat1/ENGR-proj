# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 10:01:00 2020

@author: avari
"""

import numpy as np
import matplotlib.pyplot as plt
#file = input('Enter name of file: ')
#file = "black&white.png"
dog_pic = plt.imread(input("Enter file name: "))
pixel_array = np.array(dog_pic)
pixel_array = pixel_array[:,:,0]
#changes from 3D to 2D array
pixel_array = 255*pixel_array

new = 0
print(pixel_array)
#initializes new pixel value    

x = pixel_array.shape
#copies size of the original picture
newx_array = np.zeros(x)
#creates new empty array same size as the original picture
for i in range (2, x[0]-1):
#loops through columns of picure array
    for j in range (2, x[1]-1):
    #loops through rows of picture array
        new+=pixel_array[i-1][j-1]*-1
        new+=pixel_array[i][j-1]*-2
        new+=pixel_array[i+1][j-1]*-1
        #multiplies all the columns one before the chosen pixel and adds them to the new value
        
        new+=pixel_array[i-1][j+1]*1
        new+=pixel_array[i][j+1]*2
        new+=pixel_array[i+1][j+1]*1
        #multiplies all the columns one after the chosen pixel and adds them to the new value
        
        newx_array[i][j] = new
        #sets value of new pixel as the added values
        new = 0
        #resets value of new for next pixel
plt.figure()
plt.imshow(np.uint8(newx_array), cmap='gray')
#plots new picture

new = 0
#initializes new pixel value 

y = pixel_array.shape
#copies size of the original picture
newy_array = np.zeros(y)
#creates new empty array same size as the original picture
for i in range (2, y[0]-1):
#loops through columns of picure array
    for j in range (2, y[1]-1):
    #loops through rows of picture array
        new+=pixel_array[i-1][j-1]*-1
        new+=pixel_array[i-1][j]*-2
        new+=pixel_array[i-1][j+1]*-1
        #multiplies all the rows one before the chosen pixel and adds them to the new value
        
        new+=pixel_array[i+1][j-1]*1
        new+=pixel_array[i+1][j]*2
        new+=pixel_array[i+1][j+1]*1
        #multiplies all the rows one after the chosen pixel and adds them to the new value
        
        newy_array[i][j] = new
        #sets value of new pixel as the added values
        new = 0
        #resets value of new for next pixel
        
plt.figure()
plt.imshow(np.uint8(newy_array), cmap='gray')
#plots new picture