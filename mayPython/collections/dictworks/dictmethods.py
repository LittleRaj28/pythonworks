student = {"roll":1234,"name":"hari","age":25,"course":"mca"}
#values
print(student.values())

#keys

print(student.keys())

#items -will return both keys and values

print(student.items())


for k,v in student.items():
    print(k,v)

#get(key) fetching value wrt key

#print(student["names"])

print(student.get("names"))
print("file transfer")
print("database commit")


#pop(key)

student.pop("course")
print(student)