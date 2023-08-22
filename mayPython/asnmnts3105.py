# """
# # parallel  pattern using characters
# """
# n = int(input("enter the number of levels:"))
# Y = 1
# for i in range(1,n+1):
#     for j in range(i):
#         print('',end =' ')
#         for k in range(n):
#             print(chr(64+Y), end ='  ')
#             Y += 1
#         print()
#
#  """
# alphabets in triangle shape
#  """
#
# n = 5
# # Upper Triangle
# for i in range(n):
#     for j in range(i):
#         print(chr(65 + j), end=' ')
#     print()
#
# # Lower Triangle
# for i in range(n, 0, -1):
#     for j in range(i):
#         print(chr(65 + j), end=' ')
#     print()




# Define the starting character

# Define the number of rows
# num = 5
#
# # Iterate over each row
# for i in range(num):
#     # Print spaces for each row
#     for j in range(num - i):
#         print(" ", end="")
#
#     # Print alphabets for each row
#     for k in range(i + 1):
#         print(chr(64 + k), end=" ")
#
#     # Move to the next line
#     print()


# n = int(input("enter the levels you want:"))
# y = 1
# for i in range(n+1):
#     for j in range(i):
#         print('  ',end =' ')
#     for k in range(n-1):
#         print(chr(64+y),end ='  ')
#         y += 1
#
#     print()


# Number of rows in the pyramid
num = int(input("enter the levels you want:"))

# ASCII value of 'A'
ascii= 65

# Loop to print the inverted pyramid
for i in range(num, 0, -1):
    # Print spaces for the current row
    print(' ' * (num- i), end='')

    # Print alphabets in ascending order
    for j in range(i, 0, -1):
        alphabet = chr(ascii + num- j)
        print(alphabet, end=' ')

    print()  # Move to the next line