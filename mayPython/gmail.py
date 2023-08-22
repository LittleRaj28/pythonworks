import re
# gmail=input("enter your gmail id:  ")
# g= re.search("@gmail.com$",gmail)
# if g:
#     print("it is valid..")
# else:
#     print("not valid..")


rule="[a-zA-z0-9][@gmail.com$]"
email="littleraj@gmail.com"
matcher=re.fullmatch(rule,email)
if matcher==None:
    print("valid")
else:
    print("invalid")