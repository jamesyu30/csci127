#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: October 23, 2023

import pandas as pd

csvFile = input('Enter CSV file name: ')         #Name of the CSV file
att = input("attribute: ")

tickets = pd.read_csv(csvFile)     #Read in the file to a dataframe
print("The 10 worst offenders are:")
print(tickets[att].value_counts()[:10]) #Print out the dataframe