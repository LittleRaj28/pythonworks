from re import*
text = "luminar techno lab ,luminar techno lab"
matcher = finditer("luminar",text)
count = 0
for m in matcher:
    count += 1
    print(count)