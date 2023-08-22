"""
largest of two numbers

a=33
b=200
"""
a = 99
b = 99
if b > a:
    print("b is greater than a")
elif a == b:
    print("a is equal to b")
else:
    print("a is greater than b")

"""
 write a pgm to seprate -ve and +num from the list (accept input from the user)
 """

A = [1,-1,2,-2,3,-3,4,-4,5,-5,0]
X = []
Y = []
z=[]
for i in A:
    if (i>0):
        X.append(i)
        print(X)
    elif i==0:
        z.append(i)
        print(z)
    else:
        Y.append(i)
        print(Y)


    """

write a python pgm to find largest of num
"""

    my_list = [1,10,15,3,50,40,99]
    my_list.sort()
    print(my_list)
    largest_number = my_list[0]

    for i in my_list:
        if i > largest_number:
            largest_number =i

    print("The largest number is:", largest_number

       # largest
   # my_list = [1, 10, 15, 3, 50, 40, 99]
    #my_list.sort()
    #print(my_list)
    #print(my_list[-1]


# using max function

 my_list1 = [1, 10, 15, 3, 50, 40, 99]
 max = my_list1[0]
for i in my_list1:
    if i > max:
    max = i
    print(max)









