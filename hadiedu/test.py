import csv

matrix = []

f = open('학교정보.csv', 'r')

csvReader = csv.reader(f)
for row in csvReader:
    matrix.append(row)
print(matrix[0])
f.close()
