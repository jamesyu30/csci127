#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: October 5, 2023

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv', skiprows=5)
borough = input("Enter a borough: ")

print(pop[borough].mean())
print(pop[borough].max())