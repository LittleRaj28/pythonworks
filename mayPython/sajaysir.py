# list1 = [1,2,3,4,5,8]
#
# for i in range(0,len(list1)):
#     element1 = list1[i]
#     element2 = list1[i+1]
#
#     if element2 - element1 != 1:
#          print(element1+1,"is missing")
#          break



#list comprehension

list = [3,4,5,6,7]
odds = [num for num in list if num %2!=0]
print(odds)


num_gt_five=[num for num in list if num>5]
print(num_gt_five)

evens= [num for num in list if num %2==0]
print(evens)

"""
print all numbers divisible by 3
"""

div = [num for num in list if num %3==0]
print(div)

"""
nested list
"""
list1 = [
    [1,2],
    [4,50],
    [50,45],
]

# print all numbers
for sublist in list1:
    for num in sublist:
        print(num)

allnumbers =[num for sublist in list1 for num in sublist]
print(allnumbers)

#print all numbers greater than 5

for sublist in list1:
    for num in sublist:
        if(num>5):
            print(num)

greater=[ num for sublist in list1 for num in sublist if num>5]
print(greater)


mobiles = [
    [100,"redminote12",23000,"5g"],
    [101, "oneplusnord", 32000, "5g"],
    [102, "iphone14", 123000, "5g"],
    [103, "s23ultra", 133000, "5g"],
    [104, "pixel12", 43000, "5g"],
    [105,"nothing",13000,"4g"],
    [106,"galaxya52",23000,"5g"]
]
print(len(mobiles),"mobiles available")

mobile_names = [ mob[1] for mob in  mobiles]
print(mobile_names)

#print 4g mobile phones

mobile_four_g = [ mob[1] for mob in mobiles if mob[3]=="4g"]
print(mobile_four_g)

#print mobile names below 30000

mobiles_below_thirty=[mob[1] for mob in mobiles if mob[2]<30000]
print(mobiles_below_thirty)

#print mobile names ranges between 30000 to 50000

mobiles_ranges_thirtyto = [ mob[1] for mob in mobiles if mob[2] in range(30000,50000)]
print(mobiles_ranges_thirtyto)





items = [
    [1,"pottato",45,"veg",10],
    [2, "tomato", 40, "veg", 20],
    [3, "onion", 35, "veg", 0],
    [4, "brinjal", 50, "veg", 0],
    [5, "fish", 145, "nonveg", 10],
    [6, "chicken", 145, "nonveg", 10],
    [7, "egg", 6, "nonveg", 100]
]

# total number products

for item in items:
    for num in item:
        print(num)

# print(len(items))

print(len(items))

# print in stock product names

for item in items:
    if(item[-1]>0):
        print(item[1])

instock = [item[1] for item in items if item[-1]>0]
print(instock)

#print outof stock product names

outstock = [item[1] for item in items if item[-1]==0]
print(outstock)

#print veg category product names

veg_category =  [item[1] for item in items if item[3]=="veg"]
print(veg_category)

#product available in range of 50-100

price = [ item[1] for item in items if item[2]  in range(50,100)]
print(price)

#veg products available in range of 40-80

veg_product = [item[1] for item in items if item[2] in range(40,80)]
print(veg_product)