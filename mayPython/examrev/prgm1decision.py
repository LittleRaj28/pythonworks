# write a program to check given number is odd or even

num=5

if(num%2==0):
    print("the number is even")
else:
    print("the number is odd")


# map num given a number num=if num<5 print num-1 else print num+1

num=6
if(num<5):
    print(num-1)
else:
    print(num+1)



# print num divisible by ....


num=100

if(num%3==0):
    print("fizz")
elif(num%5==0):
    print("buzz")
elif(num%15==0):
    print("fizzbuzz")

# print largest of three numbers


num1=2
num2=4
num3=6

if(num1>num2 and num1>num3):
    print("num1 is largest")
elif(num2>num1 and num2>num3):
    print("num2 is largest")
else:
    print("num3 is largest")


# leap year

year=2023

is_leapyear=False

if(year%4==0):
    is_leapyear=True
elif(year%400==0):
    is_leapyear=True

elif(year%100!=0):
    is_leapyear=False
print(year,"is leap year",is_leapyear)





