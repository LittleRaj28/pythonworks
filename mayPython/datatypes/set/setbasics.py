"""
Set
1.unchangeable,unordered,unindex,duplicates are not allowed

"""
set1 = {"Safna","12","python","BCA"}
list2 = ["bcom",]
print(set1)

y=list(set1)
print(y)
z=y[2]
print(z)

set1.add("bsc")
print(set1)
set1.update(list2)
print(set1)

set1.remove("BCA")
print(set1)

set1.discard("bcom")
print(set1)

set1.pop()
print(set1)

set1.clear()
print(set1)

#del



set5 = {"Safna","12","python","BCA",(12,23,25)}
print(set5)
a = {"12","34",6,7,246}
b = {"12",36,"34",97}
print(a.union(b))
print(a.intersection(b))
a.difference_update(b)
print(a)

"""




