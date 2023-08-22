f = open("C:\\Users\\Little Raj\\PycharmProjects\\mayPython\\fileinputoutput\\data.txt","r")
for line in f:
    print(line)

# print line by line


words = []
for line in f:
    text =line.rstrip("/n").split(" ")
    for w in text:
        words.append(w)
print(words)