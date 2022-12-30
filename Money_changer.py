#print('Enter the option you would like to do: \n 1.USD-CAD ')
option = input('Enter the option you would like to do: \n 1.USD-CAD\n 2.EUR-USD\n')
print('You choosed the option :  '+ option)  
if option == "1": 
    amountUSD_CAD = input("Enter the amount in CAD or USD (Example : 100 CAD)\n")
    last_tree = amountUSD_CAD[-3:]
    if last_tree == "CAD":
        amount_CAD = amountUSD_CAD[:-4]
        amount_USD = float(amount_CAD) * 0.74
        print("Your amount of CAD in USD is :" + str(amount_USD)) 
    elif last_tree == "USD":
        USD_amount = amountUSD_CAD [:-4]
        CAD_amount = float(USD_amount) * 1.36
        print("Your amount of USD in CAD is :" + str(CAD_amount)) 
    else:
        print("Are you sure you did it this way : 100 CAD")
elif option == "2":
    print("NICE ONE!")
else: 
    print('The only option are 1 or 2.')
    print("aaa")
