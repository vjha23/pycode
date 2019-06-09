num=[1,2,3,1,4,5,66,22,2,6,0,9]
 
list1=[]
list2=[]
print("No. greater than 5 :")
for i in num:
	if i>5 :
		print(i,",",end="")
		list1.append(i)
print("\n\nNo. less than aur Equals to 2")
for i in num:
	if i<=2:
		print(i,",",end="")
		list2.append(i)


print("\n\n")
print(list1)
print(list2)
