import re
# mob=input("enter the mobile number:")
# check=re.search("^[+]91",mob)
# if check:
#     print("it is  indian mobile number")
# else:
#     print("it is foreign number")


# landline codes

# resi=input("enter a residence number:  ")
# ekm=re.search("^0484",resi)
# ijk=re.search("^0480",resi)
# tcr=re.search("^0487",resi)
# mpr=re.search("^0494",resi)
# ksd=re.search("^04994",resi)
# cct=re.search("^0495",resi)
# if ekm:
#     print("ekm")
# elif ijk:
#     print("ijk")
# elif tcr:
#     print("tcr")
# elif mpr:
#     print("mpr")
# elif ksd:
#     print("ksd")
# elif cct:
#     print("cct")
# else:
#     print("other place")
#

# mobile number verification "+918592814568"[10-positions after +91]

mob=input("enter the mobile number:")
check=re.search("^[+]91[0-9]{10}$",mob)
if check:
    print("valid number")
else:
    print("invalid number")







