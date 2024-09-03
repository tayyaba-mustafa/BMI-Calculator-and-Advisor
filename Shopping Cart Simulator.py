#User Detail:
user = input("Enter the User name: ")
print("-" * 50)

#Detail of items purchased:
Item_name=[]
Prices=[]
Quantities=[]
while True:
    item = input("Enter the Item name: ")
    # - for end
    if item == "-" :
        break
    else:
        price = float(input(f"Enter the price of {item}: Rs."))
        quantity = float(input(f"Enter the quantity of {item}: "))
        Item_name.append(item)
        Prices.append(price)
        Quantities.append(quantity)
print("-" * 50)       

#Total Bill:
Total_bill=0
for i in range(len(Prices)):
    Total_bill += Prices[i] * Quantities[i]
print(f"Total bill = Rs.{int(Total_bill)}")
print("-" * 50) 

#Payment:
payment = int(input("Enter the amount received: Rs."))

if payment == Total_bill:
    print("Thank you for your visit!")
else:
    change =payment-Total_bill
    print(f"Change = Rs.{int(change)}")
    print("Thank you for your visit!")


