# sen = "joel,is a very good student in may batch"
# words =sen.split("  ")
# bol = sen.startswith("joel")
# print(bol)
# if bol==True:
#     print("the sentence is starting with 'joel'")
#
# if words[0]=="joel":
#     print("the sentence is starting with 'joel'")

#import packagename

import re

#startswith

# sen="joel is a very good student in may batch"
# x=re.search("^Joel",sen)
# y=re.search("^joel",sen)
# print(x)

# print(y)


 # endswith

# sen="is a very good student in may batch joel"
# x=re.search("Joel$",sen)
# y=re.search("joel$"and"joel$",sen)
# print(x)
# print(y)

#both startswith and endswith

sen="joel is a very good student in may batch"
a=re.search("Joel$",sen)
b=re.search("batch$"and"^joel",sen)
print(a)
print(b)



