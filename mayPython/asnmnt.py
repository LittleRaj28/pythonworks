my_list1 = [1,10,15,3,50,40,99]
max = my_list1[0]
for i in my_list1:
    if i >max:
        max = i
print(max)

#common numbers in two lists


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = []
for i in list1:
    if i in list2:
        common.append(i)

print("Common numbers:", common)

# print even numbers

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in num:
    if i % 2 == 0:
        print(i)

        # even and odd

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        even_numbers = []
        odd_numbers = []

        for number in numbers:
            if number % 2 == 0:
                even_numbers.append(number)
            else:
                odd_numbers.append(number)

        print("Even numbers:", even_numbers)
        print("Odd numbers:", odd_numbers)

#common list

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = []
for i in list1:
    for j in list2:
        if (i==j):
            common.append(i)
            print(common)


# write a program to remove repeated elements without using builtin method

list_to_remove=["lets","google","the","pinapple","photo","google","photo"]

com1 = []
for i in list_to_remove:
    if i not in com1:
        com1.append(i)
        print(com1)


# seperate website suffix

A =["www.zframes.com","www.wikipedia.org","www.asp.net","www.abcd.in"]
for i in A:
    suffix = i.split(".")[-1]
    print(suffix)













