#So it's alwayse repeat when error
while True :

    #print('Enter the option you would like to do: \n 1.USD-CAD ')
    option = input('Enter the option you would like to do: \n 1.USD-CAD\n 2.EUR-USD\n')
    print('You choosed the option :  '+ option)  
    if option == "1": 
    #the optiom 1 refer to the conversion from USD or CAD 
        amountUSD_CAD = input("Enter the amount in CAD or USD (Example : 100 CAD)\n")
        last_three = amountUSD_CAD[-3:]
        #last_three is for the last three charachter that the user put, this is to take USD and CAD and be able to do specific operation on it ;)
        if last_three == "CAD":
            # How much CAD you can get in USD
            #[:-4] is for taking all  the input exepct the currencies (taking number only)
            amount_CAD = amountUSD_CAD[:-4]
            amount_USD = round((float(amount_CAD) * 0.74))
            print("Your amount of CAD in USD is : " + str(amount_USD)) 
        elif last_three == "USD":
            # How much USD you can get in CAD
            USD_amount = amountUSD_CAD[:-4]
            CAD_amount = round((float(USD_amount) * 1.36))
            print("Your amount of USD in CAD is : " + str(CAD_amount)) 
        else:
            print("Are you sure you did it this way : (Example : 100 CAD)\n")
            continue
    elif option == "2":
    #the option 2 refer to the conversion from EUR or USD 
        amountEUR_USD = input("Enter the amount in EUR or USD (Example : 100 EUR)\n")   
        last_three = amountEUR_USD[-3:]
        if last_three == "EUR":
    # How much USD you can get in EUR    
            amount_EUR = amountEUR_USD [:-4]
            amount_USD = round(float(amount_EUR) * 0.93)
            print("Your amount of USD in EUR is : " + str(amount_USD))
        elif last_three == "USD":
    # How much EUR you can get in USD
            amount_USD = amountEUR_USD [:-4]
            amount_EUR = round(float(amount_USD) * 1.07)
            print("Your amount of EUR in USD is : " + str(amount_EUR))
        else:
            print("Are you sure you did it this way : (Example : 100 EUR)\n")
            continue
    else: 
        print('The only option are 1 or 2.') 
        continue
    break
    """TODO : do new currencies, could also connect to data base for real time prices.Do the round for 0.5"""