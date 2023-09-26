#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: September 20, 2023

import matplotlib.pyplot as plt
import numpy as np

size = int(input("Enter: "))
msg = input("Enter: ")

img = np.ones((size, size, 3))#DOUBLE PARENTHESES
img[1::2, :, 2:3] = 0 #if its white, set channel to 0. If black, then set channel to 1
img[::2, :, 1:2] = 0

#plt.imshow(img)
#plt.show()

plt.imsave(msg, img)