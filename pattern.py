print("Half pyramid of stars(*):")
n = int(input("enter thr number of loops:"))
for i in range (n):
    for j in range(i + 1):
        print("*" , end =  "")
    print()