import pandas as pd
import numpy as np
from pyodide.http import open_url
url = ("https://raw.githubusercontent.com/pranav-cholleti/codes/main/Drivers%20-%20Sheet1.csv")
data_set=pd.read_csv(open_url(url))
#print("Here is the list of hospitals with given required facilities.")
print(data_set)
print()
print()
#print(data_set.iloc[0,:])
#location = input("Enter your location: ")

min_dist_index=-1
min_dist=1000
for x in range(len(data_set.index)):
    if (data_set.iloc[x]['Ambulances'])==0:
      continue;
    else:
      if(data_set.iloc[x]['Distance'])<min_dist:
        min_dist=data_set.iloc[x]['Distance']
        min_dist_index=x

print("The ambulance is coming from ",data_set.iloc[min_dist_index]['Hospitals'])
print("The driver name is ",data_set.iloc[min_dist_index]['Driver'],"and the ambulance is currently ",min_dist," km from your current location.")
print("The driver contact is ",data_set.iloc[min_dist_index]['Contact'],".")
print(" ")
print(" ")
print("The hospital is booked from your selected location.")
print("Please take care")
