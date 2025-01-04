def add (P,Q):
    return P + Q
def subtract (P,Q):
    return P - Q
def multiply (P,Q):
    return P * Q
def devide (P,Q):
    return P / Q

print("Please select the operation:")
print("a. add")
print("b. subtract")
print("c. multiply")
print("d. devide")

choice = input("Please enter choise a,b,c,d:")

num_1 = int(input("Please enter the first number:"))
num_2 = int(input("Please enter the second number:"))

if choice == 'a':
    print(add(num_1,num_2))
elif choice == 'b':
    print(subtract(num_1,num_2))
elif choice == 'c':
    print(multiply(num_1,num_2))
elif choice == 'd':
    print(devide(num_1,num_2))
else:
    print("This is invalid input")