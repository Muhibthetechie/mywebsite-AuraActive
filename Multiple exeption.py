try:
    num1 , num2 = eval(int("Enter 2 numbers which can be seperated by a comma:"))
    result = num1 / num2
    print("Result is ", result)

except ZeroDivisionError:
    print("Devision by zero !!!!!!!")
except SyntaxError:
    ("Enter numbers which can be sperated by a comma such as 1,2.")
except:
    print("Wrong input")
else:
    print("No exeption")
finally:
    print("This will work no matter what")