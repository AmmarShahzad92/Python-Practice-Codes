tuples=(1,2,3,4)
a,b,c,d = tuples
print(a)
print(b)
print(c)
print(d,"\n")

""" use * if the number of variable is less than the tuples then
it will assign the remaining to the variable with *, in the form of list"""
a, *b, c = tuples
print(a)
print(b)
print(c)