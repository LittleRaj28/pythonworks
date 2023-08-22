# create a list using list keyword

food=list(("biriyani","puttu","kadala","appam"))
print(food)

for f in food:
    print(f)

#change the element

food[1]="manthi"
food[3]="idiyappam"
print(food)

#append


food.append("shawarma")
print(food)

print(len(food))

for i in range(0,len(food)):
    print(food[i])




colors = ["red","green","blue","yellow"]
# print total colors

print(len(colors))

for  i in range(0,len(colors)):
    print(colors[i])


# searching

lst=[1,2,4,6,7]
element=8


if element==lst[i]:
    print("found")
else:
    print("not found")


# next method






