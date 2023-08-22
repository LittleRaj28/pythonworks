from abc import ABC,abstractmethod

class Ide(ABC):
    @abstractmethod
    def debug(self):
        pass

class Pycharm(Ide):
    def debug(self):
        print("Pycharm debug method")
class Eclipse(Ide):
    def debug(self):
        print("Eclipse debug")

pyc=Pycharm()
pyc.debug()