def fun(a, c):
    print(c+a)

def ufun(a,b):
    c=0
    c = a+b+c
    print(c)
    fun(a,c)
a=5
b=45
ufun(a, b)