"""
Tuple is immuttable,ordered,supports indexing,allows duplication
()

"""
thistuple = ("uthamnikki",32,12,"vishnu",[8,98])
print(thistuple)


#indexing

print(thistuple[3])
print(thistuple[-1])


#slicing

print(thistuple[0:2])
print(thistuple[:-1])
print(thistuple[0][1])

# conversion


y = ("little",)
print(type(y))
thistuple+= y
print(thistuple)

print(thistuple[4][0])

# remove

thistuple.list(thistuple)
print(thistuple)

#reverse

thistuple1 = ("uthamnikki",[32,12,"vishnu"])
x = list(thistuple1)
x.reverse()
print(x)
x.reverse()
print(y)

"""
1. WAP to check whether an element exist to a str

tuple1 = ("Apple",[10,20,30], (5,12,25),1,5,6,7)
"""
tuple1 = ("Apple",[10,20,30], (5,12,25),1,5,6,7)
print("Apple" in tuple1)


