class Student:
    rollno:int
    name:str
    course:str

    def __init__(self,**kwargs):
        self.rollno=kwargs.get("rollno")
        self.name=kwargs.get("name")
        self.course=kwargs.get("course")

        def get_student(self):
            print(self.rollno,self.name,self.course)

obj = Student(rollno=1000,name="Manu",course="django")
obj.get_student()
