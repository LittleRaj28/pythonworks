f = open("C:\\Users\\Little Raj\\PycharmProjects\\mayPython\\fwrite\\data.txt","w")
languages = [
    "python","java","c","c++"
]

for l in languages:
    f.write(l+"/n")

print("finished")

f.close()
