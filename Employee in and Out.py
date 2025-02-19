class  Employee:
    def __init__(self):
        print('Employee created')
    def __del__ (self):
        print("Distructor called")

def create_obj():
    print('Making object')
    obj = Employee()
    print('Function end')
    return obj
print('calling Create_obj() function...')
obj = create_obj
print('Ended...')