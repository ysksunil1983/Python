import csv
exampleFile = open('abc.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print exampleData
