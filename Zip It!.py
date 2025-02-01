s1 = [1 , 2, 3]
s2 = ['b' , 'c' , 'a']
s3 = list(zip(s1 , s2))
print(s3 , "\n")

list1 = [10,20,30,40]
list2 = [100,200,300,400]

for x,y in zip (list1 ,list2 [::-1]):
    print(x,y)


stock = ['relaince' , 'infoyc' , 'tcs']
price = [2175 , 1172 , 2750]
new_dict = {stock : price for stock , price in zip(stock , price) }
print('\n{}'.format(new_dict))