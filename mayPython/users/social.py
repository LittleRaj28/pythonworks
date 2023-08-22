# users=[
#     {"name":"hari","followers":450,"following":780}
#
# ]

f = open("C:\\Users\\Little Raj\\PycharmProjects\\mayPython\\users\\data.txt","r")
users=[]
for line in f:
   text= line.rstrip("\n")
   name,followers,following=text.split(",")
   print(name,followers,following)

