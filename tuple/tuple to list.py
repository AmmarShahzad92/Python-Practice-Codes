tuples=(1,2,3,5)
print(type(tuples))
lists = list(tuples)
print(type(lists))
print(lists)
lists.remove(3)
print(lists)
print("\n")

""" back to tuple """
tuple1 = tuple(lists)
print(type(tuple1))
print (tuple1)

""" tuple and list is also inbuilt methods its ok for small list or tuple 
    but not suitable for large as it can cause runtime errors """