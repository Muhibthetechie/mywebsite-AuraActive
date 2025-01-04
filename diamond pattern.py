nowSize = int(input("Enter the number of rows:"))
if nowSize%2==0:
    halfDiamRow = int(nowSize/2)
else:
    halfDiamRow = int(nowSize/2)
    space = halfDiamRow-1

for i in range(1, halfDiamRow + 1):
    for j in range(1,space+1):
        print(end="")
    space = space-1
    num = 1