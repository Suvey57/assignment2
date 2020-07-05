import csv

myFile = open('csvexample.csv', 'w')
with myFile:    
    myFields = ['name', 'address','age']
    writer = csv.DictWriter(myFile, fieldnames=myFields)    
    writer.writeheader()
    writer.writerow({'name' : 'George', 'address': '4312 Abbey Road','age':22})
    writer.writerow({'name' : 'John', 'address': '54 Love Ave','age':21})
