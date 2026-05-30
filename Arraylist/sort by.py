print("================================")
#in alphabetical order
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#in decending order
thislist.sort(reverse = True)
print (thislist)
print("================================")


#in numeric order
list=[1,2,3,4,5]
list.sort()
print(list)
#in decending order
list.sort(reverse = True)
print (list)
#also use reverse
list.reverse()
print(list)
print("================================")


#case insensitive
list = ["banana", "Orange", "Kiwi", "cherry"]
list.sort(key = str.lower)
print(list)
list.sort()
print(list)
print("================================")