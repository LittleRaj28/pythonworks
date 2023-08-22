"""
1. WAP to check whether an element exist to a str

tuple1 = ("Apple",[10,20,30], (5,12,25),1,5,6,7)

2. to convert a tuple to str
tuple2 = ("s","t","r","i","n","g")

3.count the number of occurence of item 50 from a tuple
tuple3 = (20,50,70,50,60)
"""
tuple1 = ("Apple",[10,20,30], (5,12,25),1,5,6,7)
print("Apple" in tuple1)


tuple2 = ("s","t","r","i","n","g")
x =''.join(tuple2)
print(x)
print(type(x))

tuple3 = (20,50,70,50,60)
x = tuple3.count(50)
print(x)


#enumerate

y = enumerate(tuple2)
v = (list(y))
print(v)

tuple4 = (3,4,5,6,0)
print(all(tuple4))
print(any(tuple4))

#length
print(len(tuple4))

