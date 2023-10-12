#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: October 12, 2023

import pandas as pd
import matplotlib.pyplot as plt

infile = input("input: ")
outfile = input("output: ")

homeless = pd.read_csv(infile)
homeless['Fraction Children'] = homeless['Total Children in Shelter']/homeless['Total Individuals in Shelter']

homeless.plot(x='Date of Census', y='Fraction Children')
#plt.show()

fig = plt.gcf()
fig.savefig(outfile)