from re import *
text ="aabdXYZ$#4968"
matcher = finditer("[^a-zA-z0-9]",text)
print(matcher)
for m in matcher:
    print(m.group())
    
