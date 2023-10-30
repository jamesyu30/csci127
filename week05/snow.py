#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: September 26, 2023

import matplotlib.pyplot as plt
import numpy as np

file = input("file name: ")

ca = plt.imread(file)   #Read in image
countSnow = 0            #Number of pixels that are almost white
t = 0.75                 #Threshold for almost white-- can adjust between 0.0 and 1.0

#For every pixel:
for i in range(ca.shape[0]):
     for j in range(ca.shape[1]):
          #Check if red, green, and blue are > t:
          if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
               countSnow = countSnow + 1

print("Snow count is", countSnow)