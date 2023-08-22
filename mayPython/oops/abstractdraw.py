from abc import ABC,abstractmethod

class Shape(ABC):
    shape_name:str
    def __init__(self,name):
        self.shape_name=name
    @abstractmethod
    def draw(self):
        pass

    class Rectangle(Shape):