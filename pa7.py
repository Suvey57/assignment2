# Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.
list1 = []
line = input("Enter the list of tuples with first name, last name and age of students and if you dont know the age enter 'none':\n")
while(line!=''):
    list1.append(tuple(line.split()))
    line = input()
total=0
count=0
for i in range(len(list1)):
    if list1[i][2]!='none':
        total = total + int(list1[i][2])
        count = count+1
avg = total/count

for i in range(len(list1)):
    if list1[i][2]!='none':
        if int(list1[i][2])>avg:
            o='old'
        else:
            o = 'young'
        print("%s %s %s"%(list1[i][0],list1[i][1],o))
