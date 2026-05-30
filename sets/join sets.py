# join 2 sets
a={8,5,2,3,0,4}
b={"f","c","va",8, 9, 0}

v = a.union(b)
print(v,"\n")

# join more than 2 sets
a1 = {"Taha","Ibrahim", "Usman"}
print(a1,"\n")

b1 = a | b | a1
print(b1,"\n")

# unvert set1  to set2
v.update(b1)
print(v,"\n")

# print common factors
a3 = a1.intersection(b1)
print(a3,"\n")

# the item that is not available
a4 = b1.difference(a3)
print(a4,"\n")

# update the value that are not in a3
a.difference_update(b)
print(a,"\n")