class Parent:
    def mobile(self):
        print("samsung a18")

    def car(self):
        print("swift")

    def bike(self):
        print("passion")


class Child(Parent):
    pass
obj =Child()
obj.mobile()
obj.car()
obj.bike()