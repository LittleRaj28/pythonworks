"""
 a company decided to give 5% bonus to employee if he has more than 5 years of service
 """

salary = int(input("enter the salary"))
service = int(input("year of service"))

if service >=5:
    salary = salary+salary*0.05
    print("bonus =",salary)
    print("eligible for bonus")
else:
    print("not eligible for bonus")

"""(program2)"""
"""
green = allowed to go
yellow = wait
red = to stop 
"""
light = input("enter the light")

if  light == "green":
    print("car is allowed to go")
elif light == "yellow":
    print("the car need to wait")
elif light == "red":
    print("stop")
else:
    print("go to hell")

"""
A school has following rules for grading system:
    a. Below 25 - F
    b. 25 to 45 - E
    c. 45 to 50 - D
    d. 50 to 60 - C
    e. 60 to 80 - B
    f. Above 80 - A
    Ask user to enter marks and print the corresponding grade.
"""
print("------program5-----")
mark = int(input("enter your marks:"))

if mark <= 25:
    print("F")
elif mark > 25 and mark < 45:
    print("E")
elif mark > 45 and mark <50:
    print("D")
elif mark> 50 and mark<60:
    print("C")
elif mark >60 and mark<80:
    print("B")
elif mark >80:
    print("A")
else:
    print("bei")


"""
take three int values from user anf print greatest among them
"""

num1  = int(input("enter the first no"))
num2 = int(input("enter the second no"))
num3 = (int(input("enter the third no"))
if num1>num2 and num1>num>3:
    print("num1 is largest")
elif num2>num3:
    print("num2 is largest")
elif num3>num1:
    print("num3 is largest")
else:
print("number is equal")




"""
2.check the no is divible by 2 and 5
"""
number = int(input("enter the number"))
if number % 2 == 0 and number % 3 == 0:
    print("The number is divisible by both 2 and 3.")
elif number % 2 == 0:
    print("The number is divisible by 2.")
elif number % 3 == 0:
    print("The number is divisible by 3.")
else:
    print("The number is not divisible by 2 or 3.")

"""
  
check  whether the triangle is equivalent,isosceles or normal 
"""

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 == side2 == side3:
    print("The triangle is an equilateral triangle.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is an isosceles triangle.")
else:
    print("The triangle is a scalene triangle.")


