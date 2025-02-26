class student:
    __schoolname = 'XYZ school'
    def __init__(name , age , self):
        self._name = name
    def __display(self):
        print("This is a private method.")
std = (student , 25)
print(std.__schoolname)