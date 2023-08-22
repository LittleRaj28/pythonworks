"""
java var rule
starting with an alphabet
special$
length limit 1,10

"""
from re import*
rule ="[a-zA-Z][a-zA-Z0-9_$]{1,10}"
var_name="n"
matcher = fullmatch(rule,var_name)
print("invalid "if matcher==None else "valid")