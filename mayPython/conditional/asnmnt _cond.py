"""
1.whether the number is positive,negative or not
"""
number = int(input("enter the number"))
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

"""
2.check the no is divisible by 2 and 5
"""
number = int(input("enter the number"))
if number % 2 == 0 and number % 5 == 0:
    print("The number is divisible by both 2 and 5")
elif number % 2 == 0:
    print("The number is divisible by 5")
elif number % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 2 or 5")


"""

3.check whether the triangle is equivalent,isosceles, or normal triangle
"""


A= float(input("Enter the length of side 1: "))
B= float(input("Enter the length of side 2: "))
C= float(input("Enter the length of side 3: "))
# Check if the triangle is isosceles
if A== B or B== C A== c:
    print("The triangle is isosceles.")
else:
    print("The triangle is not isosceles.")

# Check if the triangle is equilateral
if si == side2 == side3:
    print("The triangle is equilateral.")
else:
    print("The triangle is not equilateral.")