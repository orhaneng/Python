import TradeManagement

trade = TradeManagement.TradeManagement()
    '''
    Trade Management Command Line UI
    '''
while (True):
    '''
    Main UI Menu

    Interface for Trade Management Class

    Uses int as option selection and str as inputs
    '''
    print("welcome to Asset  Trading  Application")
    print("1-New customer")
    print("2-Login Customer")
    print("0-Exit")
    login = False
    answer = input("enter your choice:")
    if answer == "1":
        '''
        Creates a new customer and then appends it to customerList
        str : name,
        str : SSN,
        str : password
        '''
        name = input("enter your name:")
        SSN = input("enter your SSN:")
        password = input("enter your password:")
        answer = input("press 1 to confirm your information or 0 to exit:")
        if answer == "1":
            trade.createCustomer(name, SSN, password)
            answer = input("press 1 to continue or 0 to exit:")
            if answer == "1":
                continue
            else:
                print("thank you!")
                break
    elif answer == "0":
        #exits application
        break
    elif answer == "2":
        '''
        Login
        Authenticates with SSN and password
        str : SNN
        str : password
        '''
        SSN = input("enter your SSN:")
        password = input("enter your password:")
        login = trade.loginCustomer(SSN, password)
        if (not login):
            print("unsuccessful login!")
            break
        while (login):
            #User level options
            print("1-Create Account")
            print("2-Deposit money")
            print("3-Withdraw money")
            print("4-Buy Asset")
            print("5-Sell Asset")
            print("6-List account")
            print("0-Exit")
            answerLogin = input("enter your choice:")
            if answerLogin == "0":
                #exit
                break
            elif answerLogin == "1":
                #createAccount
                accountname = input("enter your account name:")
                amount = input("account amount:")
                answerLogin = input("press 1 to confirm your information or 0 to exit:")
                if answerLogin == "1":
                    trade.createAccount(SSN, accountname, amount)
                    answerLogin = input("press 1 to continue or 0 to exit:")
                    if answerLogin == "1":
                        continue
                    else:
                        print("thank you!")
                        break
                else:
                    print("thank you!")
                    break
            elif answerLogin == "2":
                #depositMoney
                accountname = input("enter your account name:")
                amount = input("account amount:")
                answerLogin = input("press 1 to confirm your information or 0 to exit:")
                if answerLogin == "1":
                    trade.depositMoney(amount, SSN, accountname)
                    answerLogin = input("press 1 to continue or 0 to exit:")
                    if answerLogin == "1":
                        continue
                    else:
                        print("thank you!")
                        break
                else:
                    print("thank you!")
                    break
            elif answerLogin == "3":
                #withdrawMoney
                accountname = input("enter your account name:")
                amount = input("account amount:")
                answerLogin = input("press 1 to confirm your information or 0 to exit:")
                if answerLogin == "1":
                    trade.withdrawMoney(amount, accountname)
                    answerLogin = input("press 1 to continue or 0 to exit:")
                    if answerLogin == "1":
                        continue
                    else:
                        print("thank you!")
                        break
                else:
                    print("thank you!")
                    break
            elif answerLogin == "4":
                #buyAsset
                accountname = input("enter your account name:")
                type = input("enter asset type(BITCOIN;CURRENCY;ETHERIUM;STOCKS;BOND;RIPPLE):")
                print(type + " price=" + str(trade.getPrice(type)))
                amount = input("enter asset amount:")
                answerLogin = input("press 1 to confirm your information or 0 to exit:")
                if answerLogin == "1":
                    trade.buyAsset(SSN, accountname, type, amount, trade.getPrice(type))
                    answerLogin = input("press 1 to continue or 0 to exit:")
                    if answerLogin == "1":
                        continue
                    else:
                        print("thank you!")
                        break
                else:
                    print("thank you!")
                    break
            elif answerLogin == "5":
                #sellAsset
                accountname = input("enter your account name:")
                type = input("enter asset type(BITCOIN;CURRENCY;ETHERIUM;STOCKS;BOND;RIPPLE):")
                print(type + " price=" + str(trade.getPrice(type)))
                amount = input("enter asset amount:")
                answerLogin = input("press 1 to confirm your information or 0 to exit:")
                if answerLogin == "1":
                    trade.sellAsset(SSN, accountname, type, amount, trade.getPrice(type))
                    answerLogin = input("press 1 to continue or 0 to exit:")
                    if answerLogin == "1":
                        continue
                    else:
                        print("thank you!")
                        break
                else:
                    print("thank you!")
                    break
            elif answerLogin == "6":
                #List account of Assets
                answerLogin = input("press 1 to confirm your information or 0 to exit:")
                if answerLogin == "1":
                    trade.customerAccountList(SSN)
                    answerLogin = input("press 1 to continue or 0 to exit:")
                    if answerLogin == "1":
                        continue
                    else:
                        print("thank you!")
                        break
                else:
                    print("thank you!")
                    break
            else:
                break
