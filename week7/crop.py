#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: October 14, 2023

import matplotlib.pyplot as plt

inputfile = input("Enter input: ")
outputfile = input("Enter output: ")


img = plt.imread(inputfile)

#plt.imshow(img)
#plt.show()

img2 = img[img.shape[0]//2:, :img.shape[1]//2]       

#plt.imshow(img2)       
#plt.show()               

plt.imsave(outputfile, img2) 