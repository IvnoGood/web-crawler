import csv


def ToCSV(filename, url, title, paragraphs):
    paragraphs = paragraphs[0]
    content = [url, title, paragraphs]

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(content)
        print("written !")
