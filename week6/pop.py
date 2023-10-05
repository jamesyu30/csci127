#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: October 5, 2023

import matplotlib.pyplot as plt
import pandas as pd

#Open the CSV file and store in pop
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

borough = input("Enter a borough: ")
filen = input("Enter a file: ")

#Compute the fraction of the population in the Bronx, and save as new column:
pop['Fraction'] = pop[borough]/pop['Total']

#Create a plot of year versus fraction of pop. in Bronx (with labels):
pop.plot(x = 'Year', y = 'Fraction')

#Save to the file:  fractionBX.png
fig = plt.gcf()
fig.savefig(filen)