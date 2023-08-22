"""

list are mutable,ordered,supports indexing, allows duplication

"""
list_items = ["apple","orange","mango","grapes"]
print(list_items)

#indexing
print(list_items[2])
print(list_items[3])

#slicing
print(list_items[:4])
print(list_items[:-2])
print(list_items[:3])
print(list_items[0][-1])
print(list_items[-1])
print(list_items[:2:-1])
print(list_items[:1:-1])

#update
list_items[1]="pineapple"
print(list_items)


#converting to string

str1 = 'hi little'

x = list(str1)
print(x)
x[1]='ey'
print(x)

print("".join(x))


#nesting of list

list_items = ["apple","orange","mango","grapes",["python","java","php","linux"]]

#sorting of nested list

x = ["python","java","php","linux"]
x.sort(reverse=True)
print(x)
print(list_items[4])
print(list_items[4][0])
print(list_items[4][2][2])

#updating nested list
list_items[4][1] = 'angular'
print(list_items)

#append

list_items.append('vue.js')
print(list_items)

#insert

list_items[4].insert(1,'golang')
print(list_items)

#remove

list_items.remove("apple")
print(list_items)

#pop
list_items.pop(2)
print(list_items)

#clear

list_items.clear()
print(list_items)

#delete


# reverse

list1 = ["vishnu","cherry","utham"]
print(list1)
list1.reverse()
print(list1)

#sort

list1.sort()
print(list1)

#extend

list2 = ["volvo","bmw"]
list2.extend(list1)
print(list2)

#count

x= list1.count("cherry")
print(x)

