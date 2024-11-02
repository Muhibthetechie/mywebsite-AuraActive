actual_price = float(input("Please enter the actual amount: "))
sale_amount = float(input("Please enter the sales amount:"))
if (sale_amount > actual_price):
    amount = sale_amount - actual_price
    print("total profit = {0}".format (amount) )
else:
    print("No profit !!!")