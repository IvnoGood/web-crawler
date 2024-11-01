
# importing library
import csv
 
# opening the csv file in 'w' mode
file = open('g4g.csv', 'w', newline ='')
 
with file:
    # identifying header  
    header = ['Organization', 'Established', 'CEO']
    writer = csv.DictWriter(file, fieldnames = header)
     
    # writing data row-wise into the csv file
    writer.writeheader()
    writer.writerow({'Organization' : 'Google', 
                     'Established': '1998', 
                     'CEO': 'Sundar Pichai'})
    writer.writerow({'Organization' : 'Microsoft', 
                     'Established': '1975',
                     'CEO': 'Satya Nadella'})
    writer.writerow({'Organization' : 'Nokia',
                     'Established': '1865',
                     'CEO': 'Rajeev Suri'})