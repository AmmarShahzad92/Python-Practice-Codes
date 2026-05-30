class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def names(self):
        print(self.name,"\n",self.age)

s1 = student("Taha",12)
s1.names()