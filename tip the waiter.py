def total_cacl(bill_amount,tip_perc):

    Total = bill_amount*(1 + 0.01*tip_perc)
    Total =round(Total,2)
    print(f"Please pay ${Total}")
total_cacl(235,32)