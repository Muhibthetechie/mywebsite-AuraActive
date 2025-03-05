from abc import ABC, abstractmethod

class ABsclass(ABC):
    def print(self , x):
        print("The passed value is" , x)
    def task(self):
        print("We are inside the ABCclass.")
class test_class(ABsclass):
    def task(self):
        print("We are in the text_class")
test_obj = test_class()
test_obj.task()
test_obj.print(100)