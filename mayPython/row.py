n = int(input("enter the levels you want:"))
for i in range(1,n+1):#rows 1,2.....6
    for j in range(n-i):#spacing
        print('$',end ='')
    for k in range(i):
            print('*  ',end ='')
    print()

    #reverse

n = int(input("enter the levels you want:"))
for i in range(n+1):
    for j in range(i):
        print('',end ='')
    for k in range(n-i):
            print('*  ',end ='')
    print()
#pyramid using numbers

n = int(input("enter the levels you want:"))

for i in range(1, n + 1):  # rows 1,2.....6
    for j in range(n-i):
        print('', end='')
    for k in range(i):
        print(k , end='')
    print()