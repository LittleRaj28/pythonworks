class P1:
    def m1(self):
        print("class of m1 method")

class P2:
    def m1(self):
        print("class of m2 method")

class C1(P2,P1):
    pass
c=C1()
c.m1()