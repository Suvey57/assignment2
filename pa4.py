a=[]
b=int(input("enter number of colleagues to be added to the list::"))
for i in range(b):
    c=input("enter the name of the colleagues that need to be added to the list::")
    a.append(c)
print(a)
a.sort()
print(a)
print("the first item on list is{}",a[0])
print("the second item on list is{}",a[1])