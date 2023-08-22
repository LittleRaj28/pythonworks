class Student:
    rollno:int
    name: str
    course:str
def __init__(self,roll,name,course):
    self.rollno=roll
    self.name=name
    self.course=course

def get_student(self):
    print(self.rollno,self.name,self.course)

obj1 = Student(1000,"Hari","Django")
obj1.get_student()

obj2 =Student(1001,"Manu","Mearn")
obj2.get_student()