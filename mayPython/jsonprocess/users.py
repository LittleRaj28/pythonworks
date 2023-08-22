
from json import load

f= open("C:\\Users\\Little Raj\\PycharmProjects\\mayPython\\jsonprocess\\data.json","r")

data= load(f)
print(data)

for u in data:
    names=u.get("name")
    print(names)

# students with maximum marks
# lst =[10,30,40]


candidate = max(data,key=lambda s:s.get("total"))
print(candidate)

# sort all students wrt total ordr by desc

sorts= sorted(data,reverse=True,key =lambda s:s.get("total"))
print(sorts)


# print bca students

for u in data:
   if u.get("course")=="bca":
       print(u.get("name"))
f.close()




