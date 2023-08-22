"""
starts with ana alphabet
any number of alphabets and digits

"""
from re import*
rule = "[a-zA-z][a-zA-Z0-9]*"
var_name = ""
matcher = fullmatch(rule,var_name)
if matcher==None:
    print("valid")
else:
    print("invalid")