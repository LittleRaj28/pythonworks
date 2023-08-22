st ={1,2,3,4,5,6}
st.add(100)
print(st)

#adding an object into set

# class list:
#     append()
#
#     pop()
#
#     class set:
#         add()

list = [1,2,3,4,5,6]
sets = set(list)
print(sets)

set1 = {10,11,12,13}
set2 = {10,12,25,30}

union_set = set1.union(set2 ) #union
print(union_set)

intersect_set = set1.intersection(set2)  # intersection
print(intersect_set)

difference_set = set1.difference(set2)     #difference
print(difference_set)


