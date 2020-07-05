a=int(input("enter the number of friends whose info is to be added to list:"))
b=[]
for i in range(a):
    c = (input("Enter ur first name:"),input("Enter ur last name:"),int(input("Enter ur age:")))
    (first_name, last_name, age) = c
    b.append(c)
    print(c)
print(b)
b.sort(key=lambda tup: tup[1])
print(b)
#sorted_by_second = sorted(data, key=lambda tup: tup[1])
#print(sorted_by_second)
