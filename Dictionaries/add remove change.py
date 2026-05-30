dicts={
    "name":"John",
    "age":30,
    "city":"New York"
}
#update
dicts.update({"name":"Taha"})
print(dicts,"\n")

dicts.update({"region": "Pakistan"})
print(dicts,"\n")

dict1 = dicts.copy()
print(dict1)

#remove item
dict1.pop("region")
print(dict1,"\n")

# nested dictionaries
dict1={ 
    "s1":{
        "name":"John",
        "age":30
    },
    "s2":{
        "name":"Alice",
        "age":25
    },
    "s3":{
        "name":"Bob",
        "age":35
    }
}

for y in dict1.values():  #print using loops
    print(y)
print("--------------------------------")

for a,b in dict1.items():  #print using loops with it is is nested and seperation using item, key method
    print(a)
    print(b)
print("--------------------------------")

