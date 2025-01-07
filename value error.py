try:
    number = int(input("Enter a integar:"))
    print("The number entered is",number)
except ValueError as ex:
    print("Exeption:",ex)