userAccounts = []


def showAccounts():
    print(userAccounts)
    startAccount()


def startAccount():
    accountOptions = input(
        'Press 1: Create account \n Press 2: Transaction \n press 3: Show Accounts \n press 4: To exit app \n: ')
    if (accountOptions == "1"):
        createAccount()
    elif (accountOptions == "2"):
        transaction = input(
            'press 1: Check Balance \n press 2: Withdraw \n press 3: Transfer \n')
        if(transaction == '1'):
            checkBalance()
        elif(transaction == '2'):
            withdrawMoney()
        elif(transaction == '3'):
            transferMoney()
        else:
            startAccount()

    elif(accountOptions == "3"):
        showAccounts()
    elif(accountOptions == '4'):
        return
    else:
        print('invalid input, if you wish to exit press 4')
        showAccounts()


def withdrawMoney():
    user = input('enter email associated with your account: ')
    if(userExists(user)):
        withdrawal = input('please enter an amount to withdraw: ')
        if(int(withdrawal) > int(userDetails(user)[2])):
            print('your account is too low for withdrawal!!')
            startAccount()
        else:
            amountToWithdraw = int(withdrawal)
            totalAmountLeft = int(userDetails(user)[2]) - amountToWithdraw
            if(setNewAmount(totalAmountLeft, user)):
                print('you have withdrawn ' + 'N' + str(withdrawal) +
                      '. You have N' + str(totalAmountLeft)+' left')
            startAccount()


def setNewAmount(amount, user):
    for i in userAccounts:
        if(userExists(user)):
            i['amount'] = amount
            return True


def userExists(user):
    if(len(userAccounts) == 0):
        print('no account found for this user!' + '\n')
        return False
    else:
        for i in userAccounts:
            if(i['email'] == user):
                return True
            else:
                print('user doesnt not exist.. please create an account \n')
                return False


def userDetails(user):
    for i in userAccounts:
        if(i['email'] == user):
            return [i['email'], i['password'], i['amount']]


def transferMoney():
    user = input('enter email associated with your account: ')
    if(userExists(user)):
        transfer = input('please enter an amount to transfer: ')
        if(int(transfer) > userDetails(user)[2]):
            if(setNewAmount(transfer, user)):
                print('Transfer successful!!')
                startAccount()
        else:
            print('You cannot transfer this amount!!')
            startAccount()


def checkBalance():
    user = input('please enter your email associated with account: ')
    if(userExists(user)):
        print("You have a total of" + " N" + str(userDetails(user)[2]) + '\n')
        startAccount()


def validateAccount(email, password):
    for i in userAccounts:
        if i['email'] == email:
            print('email already exists...')
            startAccount()
        elif i['password'] == password:
            print('password already exists...')
            startAccount()
    return True


def createAccount():
    global userAccounts
    email = input('please enter a unique email: ')
    password = input('please enter a password: ')

    length = len(userAccounts)
    print(str(length) + ' accounts')
    if len(userAccounts) == 0:
        account = {}
        account['email'] = email
        account['password'] = password
        account['amount'] = 0
        userAccounts.append(account)
        print(
            'successfully added'
        )
        print(userAccounts)
        startAccount()

    elif len(userAccounts) > 0:
        validate = validateAccount(email, password)
        if (validate):
            account = {}
            account['email'] = email
            account['password'] = password
            userAccounts.append(account)
            print('successfully inserted to end')
            startAccount()
        else:
            print('')


startAccount()
