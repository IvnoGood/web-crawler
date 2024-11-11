import csv

paragraphs = ["The CornHub team is always updating and adding more corn videos every day. It's all here and 100% free corn. We have a huge free CCC video selection that you can download or stream. CornHub is the most complete and revolutionary corn tube site. We offer streaming corn videos, CCC photo albums, and the number 1 free popping community on the net. We're always working towards adding more features that will keep your love for corno alive and well. Send us feedback if you have any questions/comments.", 'CornHub is a CO2 Net Zero website', '© CornHub.website, 2024']

paragraphs = paragraphs[0]

print(paragraphs)
# Data you want to add as a new row
new_row = ["John", "Doe", 30, paragraphs]

# Open the CSV file in append mode
with open('your_file.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(new_row)

print("Row added successfully!")
