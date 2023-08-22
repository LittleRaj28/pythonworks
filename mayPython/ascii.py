# A = 65
for i in range(97,123):
    print(chr(i),end=" ")

# import string

# for i in string.ascii_uppercase:
#     print(i,end ="\n")


"""
qns
"""

# num = int(input("enter the number of rows:"))
#
# for i in range(1,num):
#     for j in range(i):
#         print(j,end ="")
#     print()

# num = int(input("enter the number of rows:"))
#
# for i in range(1, num):
#     for j in range(i):
#         print('*  ', end="")
#     print()

# num1 = int(input("enter the number of rows:"))
# k = 1
# for i in range(1,num1):
#     for j in range(i):
#         print(chr(64+k),end ="")
#         k+=1
#     print()
#
# """
# alphabets using pyramids
# """
#
# for i in range(65,70):
#     for j in range(65,i+1):
#         print(chr(j), end='')
#     print()


"""
parallel  pattern using characters
"""
n = int(input("enter the number of levels:"))
Y = 1
for i in range(1,n+1):
    for j in range(i):
        print('',end =' ')
    for k in range(n):
        print(chr(65+Y),end ='   ')
        Y += 1
    print()

