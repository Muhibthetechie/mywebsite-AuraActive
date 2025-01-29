import array as arr
array_num = arr.array ('i' , [1,1,2,4,3,4,5,6,4])
print("Original array:" + str(array_num))
print("Number of occerences of number 3 in the array is: "+str(array_num.count(3)))
array_num.reverse()
print("Reverse the number of items:")
print(str(array_num))