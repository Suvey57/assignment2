# import csv
# with open("csvexample.csv", "r") as f:
#     reader = csv.DictReader(f)
#     a = list(reader)
#     print(a)


import csv
with open('csvexample.csv') as f:
    reader = csv.reader(f, skipinitialspace=True)
    header = next(reader)
    a = [dict(zip(header, map(str, row))) for row in reader]
print(a)    
