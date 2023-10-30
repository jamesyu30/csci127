#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: October 29, 2023

import pandas as pd

csvFile = input('Enter CSV file name: ')         #Name of the CSV file

coll = pd.read_csv(csvFile)
print(coll["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])
