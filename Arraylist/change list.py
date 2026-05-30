list=[1,2,3,4,5,6]
list[1]=10
print(list)

list.insert(1,85)
print(list)

# add items to the list
list.append(55)
print(list)

#addition of two lists
mlist=["Taha","Micheal","Alexander"]
list.extend(mlist)
print(list)

#remove from list by name
list.remove("Micheal")
print(list)

#remove from list by index number
list.pop(1)
print(list)

#clear item from the list
list.clear()
list.insert(0, "Taha")
print(list)

""" #remove the temps from the list
del list
print(len(list)) """
