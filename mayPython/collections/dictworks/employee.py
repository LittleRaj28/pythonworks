emp = {"id":101,"Name":"Little","designation":"HR","salary":250000}
print(emp)

#print name

print(emp["Name"])

# print salary

print(emp["salary"])

# iterating dictionaries

for key in emp:
    print(key,emp[key])

 #adding new key

emp["gender"]="male"
print(emp)

# updating a value

emp["salary"]=27000
print(emp["salary"])
print(emp)

#update salary with current salary +2000

emp["salary"]+=2000
print(emp["salary"])

#key in dictionary is present or not present

if("Name"in emp):
    print("present")
else:
    print("not present")


