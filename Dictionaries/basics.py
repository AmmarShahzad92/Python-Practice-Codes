dicts={
    "name":"John",
    "age":30,
    "city":"New York"
}

print(dicts)

print(dicts["age"])

""" duplication not allowed in case of duplication the next will be used """

dicts={
    "name":"John",
    "age":30,
    "age":25,
    "city":"New York"
}
print(dicts) # whole dictionary

print(dicts["age"]) # specific dictionary

print(len(dicts))  #length of dictionary

print(type(dicts)) #data type

print(dicts.get("City")) #use get

print(dicts.keys()) #keys intered in dictinarty
print(dicts.values()) #values intered in dictionary
dicts["city"]= "attock" # change value of a key
print(dicts["city"])
print(dicts.items())    #get dictionary in terms of items


