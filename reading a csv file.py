import csv

with open('GOOG.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    #next(csv_reader)  skiping the first line
    for line in csv_reader:
        print (line[:])