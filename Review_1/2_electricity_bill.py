def calculate_bill(units):
    bill_amount=0
    if units<100:
        bill_amount=units*10
        return bill_amount
    elif units<200 and units>100:
        bill_amount=(100*10)+(units-100)*15
        return bill_amount
    elif units<300 and units>100:
        bill_amount=(100*10)+(100*15)+(units-200)*20
        return bill_amount
    else:
        bill_amount=(100*10)+(100*15)+(100*20)+(units-300)*25
        return bill_amount
        
        

bill_units=int(input("enter the number of electricity units: "))
payable_bill=calculate_bill(bill_units)
print(f"electriciy bill is {payable_bill}")