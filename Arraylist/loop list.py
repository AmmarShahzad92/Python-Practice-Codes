#print all the list 
list=[0,2,3,4,5,6]
for x in list:
    print(x, end=' ')
print("\n")

#print list of all the items in the list by len method
list=[1,2,3,4,5,6]
for x in range(len(list)):
    print(list[x], end=" ")
print("\n")

#list by using while loops

list=["Taha","Usman","ibrahim"]
i=0
while i<len(list):
    print(list[i], end=" ")
    i=i+1
print("\n")

#list condition in Python
list=[1,2,3,4,5,6]
mlist=[x for x in list if x<5]
print(mlist)