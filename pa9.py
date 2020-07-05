def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found

a=[9,6,8,1,2,4,5,0]
print(a)
a.sort()
print(a)
b=int(input("enter the value to be searched::"))
print(binary_search(a, b))

