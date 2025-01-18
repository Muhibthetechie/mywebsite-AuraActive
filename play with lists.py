L = [1204,1944,3445,1011,2222,1246,100,122223]
print("Original lists:", L)

count = 0

for i in L:
    count += 1

avg = count/len(L)
print("Sum = ",count)
print("Avrage:", avg)

print("The smallest number in the list is ",L[0])
print("The largest number in the list is ",L[-1])