import csv

matrix = []

f = open('장애인편의.csv', 'r')
csvReader = csv.reader(f)

for row in csvReader:
    matrix.append(row)
print (matrix[0])
f.close()
