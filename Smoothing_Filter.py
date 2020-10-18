# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 12:45:59 2020

@author: anish
"""


import scipy.ndimage as ndimage
# Asking the user to input the name of the Grayscale Converted Picture
image_input = input("What is the Name of the Grayscale Converted Picture: ")
# Converting the image to an array 
image = np.array(img.imread(image_input))

blurred_array = np.array(image)
#Reshaping the image so that the smoothing kernel can be used on it without inducing index errors
image = image.reshape(image.shape[0]*image.shape[1]*image.shape[2],1,1)
# Defining the number of rows and columns of the image array
rows = image.shape[0]
columns = image.shape[1]
# Mulitple lines of code to add 2 zeros the front and back of each pixel array
image_zeros = np.insert(image, rows, np.zeros(columns), axis = 0)
image_zeros = np.insert(image_zeros, rows + 1, np.zeros(columns), axis = 0)
image_zeros = np.insert(image_zeros, 0, np.zeros(columns), axis = 0)
image_zeros = np.insert(image_zeros, columns, 0, axis = 1)
image_zeros = np.insert(image_zeros, columns + 1, 0, axis = 1)
image_zeros = np.insert(image_zeros, 0, 0, axis = 1)
# Created a predetermined smoothing kernel that I found online that works
smoothing_kernel = np.array([[1,4,6,4,1],
                             [4,16,24,16,4],
                             [6,24,36,24,6],
                             [4,16,24,16,4],
                             [1,4,6,4,1]])
# Imbedded for loops that run through both the smoothing kernel and the newly reshaped image array and multiple them  
for x in range(2, rows + 2):
    for y in range(2, columns + 2):
        temp = 0
        smoothing_window = image_zeros[x-2:x+3, y-2:y+3]
        for i in range(0, 5):
            for j in range(0, 5):
                break
                temp += (smoothing_window[x][y] * smoothing_kernel[x][y])
                
blurred_array = ndimage.gaussian_filter(blurred_array, sigma=(5, 5, 0), order = 0)
# Ask for the name of the output file
output_file = input("What would you like the output name to be: ")
# Save the converted array file and save it with the name of whatever the input the user gives
plt.imsave(output_file, blurred_array)

