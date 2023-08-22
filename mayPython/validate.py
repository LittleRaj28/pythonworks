import re
# text = "abababab"
# text1= "aaaabbbbccc"
# t1 = re.search("[a]{4}",text)
# t2 = re.search("[a]{4}",text1)
# print(t1)
# # print(t2)
#
# """
# continuous 4 alphabets
# """
#
# te= "abcd12345"
# check =re.search("[a-z]{4}",te)
# print(check)
#
#
# # mobile number verification "+918592814568"[10-positions after +91]
#
# st="3457abDARG756687"
# s= re.search("[a-z]{2}[A-Z]{4}",st)
# print(s)



mobno=+9129488586788

rule="[^+91][0-9]{10}"
matcher=re.fullmatch(rule,mobno)
if matcher==None:
    print("valid number")
else:
    print("invalid")








