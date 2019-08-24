import re
import csv
import sys

text = [sys.argv[1]]

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

new_text = remove_html_tags(text[0])
new_text = new_text.replace("&quot;", "\"");
new_text = new_text.strip()
row = [new_text]

with open('clean.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(row)

csvfile.close()
