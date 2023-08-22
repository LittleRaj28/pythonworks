from abc import ABC,abstractmethod


class Employee(ABC):
    name:str
    salary:int
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @abstractmethod
    def calcualte_salary(self):
        pass
class Manager(Employee):
    def calculate_salary(self):
        print("current salary+25000")


class Developer(Employee):
    def calculate_salary(self):
        print("current salary+20000")