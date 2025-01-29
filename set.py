my_set = {1,1,2,2,3,4,5,3,2,5,4}
print(my_set)

my_set = {1,1,2,2,3,4,5,3,2,5,4}
my_set.add(7)
print(my_set)

my_set = {1.0 , "Hello", (1,1,2,2,3,4,5,3,2,5,4)}

my_set = set([1,2,3,4,3,4,5,2,1,3])
print(my_set, "\n")

num_set = set([1,2,2,1,4,3,3,4,5,6,6,5])
print("Original set:")
print(num_set)
num_set.pop()
print("After removing the first element:")
print(num_set,"\n")

setx = {"Green","Blue"}
sety = {"Red","Blue"}
print(setx)
print(sety)
print("\n Union of both set is:")
seta = setx.union(sety)
print(seta)