import csv

# Data you want to add as a new row
new_row = ["John", "Doe", 30, "Engineer"]

# Open the CSV file in append mode
with open('your_file.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    
    # Write the new row to the file
    writer.writerow(new_row)

print("Row added successfully!")
