a=[]
test=['john']
b=int(input("enter the number of data to be inputted::"))
for i in range(b):
    c=input("enter name of colleague to be inputted::")
    a.append(c)
print(a)
if a[i]==test[0]:
    print("found")
else:
    print("not found")
