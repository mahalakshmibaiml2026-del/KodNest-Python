#Dictionaries - {key:value} - key value pairs
#key is immutable but values are mutable
#values can be aything - duplicates are allowed only for values

dict1 = {"name":"Maha","age": 23,"city":"costa rica"}
print(dict1)

#overwriting or update
dict1["name"] = "Doe"
print(dict1)

#to list only keys
print(dict1.keys())

#to list only values
print(dict1.values())

#to list both key and value
print(dict1.items())

#assigning multiple valuesnto keys
dict1 = {"name":"Maha","age": 23,"city":["costa rica","usa","georgia"]}
print(dict1)
print(type(dict1),dict1["name"],dict["city"])
#to print a specific city
print(dict1["city"][1])

#constructor
#stu_info = dict()  representation of constructor in dictionary

stu_info = dict(name = "Ram", age = 30, city = "U")
#to add a key value 
stu_info["salary"] = 50000

#updating the salary - 2 ways
stu_info["salary"] = 30000
stu_info.update({"salary": 20000})


#deleting an item
stu_info.pop("age")

stu_info.popitem() # removes last added key value/item

del stu_info["city"]

#to delete the entire dictionary
stu_info.clear()

del stu_info
# print(stu_info)

# loop dicts
dict1 = {
    "name": "John",
    "age": 30,
    "city": ["New York", "USA", "Germany"]
}


#to get the keys only
for i in dict1.keys():
    print(i)

#to get the values only
for i in dict1.values():
    print(i)

# Dict Methods
print(dict1.get("name"))
print(dict1.get("salary",0))

#fromkeys
print(dict1.fromkeys(["name","age","city"]))

#setdefault
print(dict1.setdefault("name","john"))

#copy
dict2 = dict1.copy()
print(dict2)