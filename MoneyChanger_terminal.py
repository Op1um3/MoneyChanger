def convert_usd_cad(amount):
    last_three = amount[-3:]
    if last_three == "CAD":
        amount_cad = amount[:-4]
        amount_usd = round((float(amount_cad) * 0.74))
        print("Your amount of CAD in USD is: " + str(amount_usd)) 
    elif last_three == "USD":
        usd_amount = amount[:-4]
        cad_amount = round((float(usd_amount) * 1.36))
        print("Your amount of USD in CAD is: " + str(cad_amount)) 
    else:
        print("Are you sure you did it this way: (Example: 100 CAD)")
        return False
    return True

def convert_eur_usd(amount):
    last_three = amount[-3:]
    if last_three == "EUR":
        amount_eur = amount[:-4]
        amount_usd = round(float(amount_eur) * 0.93)
        print("Your amount of USD in EUR is: " + str(amount_usd))
    elif last_three == "USD":
        amount_usd = amount[:-4]
        amount_eur = round(float(amount_usd) * 1.07)
        print("Your amount of EUR in USD is: " + str(amount_eur))
    else:
        print("Are you sure you did it this way: (Example: 100 EUR)")
        return False
    return True

#So it's alwayse repeat when error
while True:
    option = input('Enter the option you would like to do:\n1. USD-CAD\n2. EUR-USD\n')
    print('You chose option: ' + option)
    if option == "1":
        amount = input("Enter the amount in CAD or USD (Example: 100 CAD)\n")
        if not convert_usd_cad(amount):
            continue
    elif option == "2":
        amount = input("Enter the amount in EUR or USD (Example: 100 EUR)\n")
        if not convert_eur_usd(amount):
            continue
    else:
        print('The only options are 1 or 2.')
        """the continue statement is used to skip the rest of the current iteration of the loop and move on to the next iteration.
        This can be useful if you want to skip certain iterations of the loop under certain conditions
        the break statement is used to exit the loop once a valid amount has been entered by the user
        continue"""
    break
    """TODO : do new currencies.Do the round for 0.5, do better function for it to be more quick to add currencies."""
    """Overview of some concept : For example, in the revised script I provided, the continue statement
     is used to skip the rest of the current iteration of the loop if the user entered the amount in the wrong format.
     In the revised script I provided, the break statement is used to exit the loop once a valid amount has been entered by the user."""