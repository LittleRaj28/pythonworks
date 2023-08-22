import datetime

class Operations:
    num1:int
    num2:int
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2

    def add(self):
        return self.num1+self.num2

    def product(self):
        return self.num1*self.num2

    @staticmethod

    def get_date():
        return datetime.date.today()

op=Operations(100,200)
print(op.add())
print(op.product())
print(Operations.get_date())







"""
 method overriding -vehicles
"""

class Parent:
    def vehicles(self):
        self.context=["passionpro","swift"]
        return self.context

class Child(Parent):
    def vehicles(self):

        self.context=super().vehicles()
        self.context.append("hunter")
        return(self.context)

        pass

c=Child()
print(c.vehicles())



