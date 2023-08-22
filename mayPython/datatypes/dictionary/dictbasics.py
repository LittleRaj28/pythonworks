"""
dictionary is mutable,ordered,duplicates are not allowed

key-valued pair
{}

keys are unique
"""
dict1 = {"name":"little ","age":21,"place":'vyttila',"course":"Python"}
print(dict1)

print(dict1["name"])
print(dict1.get("name"))
dict1["name"] = "Vishnu"
print(dict1)
dict1.update({"course":"react"})
print(dict1)
dict1.update({"qualification":"bsc","Role":"trainee"})
print(dict1)
x = dict1.keys()
print(x)
y = dict1.values()
print(y)

dict1.pop("name")
print(dict1)

dict1.popitem()
print(dict1)

x1 = ('keys1','keys2','keys3')
thisdict = dict.fromkeys(x1)
print(thisdict)


z = dict1.setdefault("name","achu")
print(z)

dict2 = {"name":"appu","age":12,"place":"kochi","course":"python"}
if "course" in dict2:
    print("true")

keys = ["ten","twenty","thirty"]
values = [10,20,30]
new_dict = dict(zip(keys,values))
print(new_dict)

dict3 = {"name":"appu","age":12,"place":"kochi","course":"python"}
dict4 = {"gender":"male"}
dict3.update(dict4)
print(dict3)