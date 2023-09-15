#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: September 14, 2023

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

inputfile = input("Enter input: ")
outputfile = input("Enter output: ")


img = plt.imread(inputfile)   #Read in image from csBridge.png

#plt.imshow(img)		                 #Load image into pyplot
#plt.show()                         #Show the image (waits until closed to continue)

img2 = img.copy()        #make a copy of our image
img2[:,:,1] = 0          #Set the green channel to 0
#img2[:,:,2] = 0          #Set the blue channel to 0

#plt.imshow(img2)         #Load our new image into pyplot
#plt.show()               #Show the image (waits until closed to continue)

plt.imsave(outputfile, img2)  #Save the image we created to the file: reds.png