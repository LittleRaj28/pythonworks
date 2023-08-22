"""

3.check whether the triangle is equivalent,isosceles, or normal triangle
"""
A = float(input("Enter the 1st side: "))
B = float(input("Enter the 2nd side: "))
C= float(input("Enter the 3rd side: "))

if A == B and B == C and A == C:
    print("The triangle is an equilateral triangle")
elif A == B or B == C or A == C:
    print("The triangle is an isosceles triangle ")
else:
    print("The triangle is a normal triangle.")

"""
Check whether a student will not be allowed to sit in exam if his/her attendence is less than 75%.
"""

attendance = int(input("Enter the attendance percentage:"))
if attendance >= 75:
    print("The student is allowed to sit in the exam")
else:
    print("The student is not allowed to sit in the exam")

"""
Find minimum number out of given number 
"""
num1 = int(input("enter the no1:"))
num2 = int(input("enter the no2:"))
num3 = int(input("enter the no3:"))
if num1 < num2 and num1 < num3:
    print("num1 is minimum")
elif num2 < num1 and num2 < num3:
    print("num2 is minimum")
elif num3 < num1 and num3 < num2:
    print("num3 is minimum")
else:
    print("closed")

"""
paliandrom
"""
number = int(input("enter the number"))
reverse =  (int(str(number)[::-1]))
if number == reverse:
      print("palindrome")
else:
    print("not palindrome")

"""
fibonacci
"""
number = 10
n1,n2 =0,1
print(n1)
print(n2)
for i in range(number):
    n3 = n1+n2
    n1=n2
    n2=n3
    print(n3)

"""
amstrong
"""
#12 = 1*1*1 + 2*2*2 = 12

num = int(input("enter the number:"))
sum = 0
temp = number
while temp > 0



"""
wap to print sum of even numbers and odd numbers
numbers = [3,6,7,5,11,8]
"""
numbers = [3,6,7,5,11,8]
odd =[]
even =[]
if numbers%2==0:
    print("even numbers")
else:
    print("odd numbers")

