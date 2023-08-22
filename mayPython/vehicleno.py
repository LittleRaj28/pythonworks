"""
KL-07-BN-4970
KL start
2 digit
alphabet2
numbers4

"""
from re import*
rule ="[K][L][-][0-9]{2}[-][A-Z]{2}[-][0-9]{4}"
veh_num = "TN-07-KH-3567"
matcher = fullmatch(rule,veh_num)
print("in valid"if matcher==None else "valid")

