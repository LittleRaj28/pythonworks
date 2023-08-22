"""
variable starting with k-m
second character should be digit divivsible by 3
any number of characters


"""

from re import*
rule= "[k-m][369][a-zA-Z0-9]*"
var_name = "k3llo"
matcher = fullmatch(rule,var_name)
if matcher==None:
    print("valid")
else:
    print("invalid")
