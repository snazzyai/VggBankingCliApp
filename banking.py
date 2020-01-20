userAccounts = []


def showAccounts():
    print(userAccounts)
    startAccount()


def startAccount():
    print('MAIN MENU')
    accountOptions = input(
        'Press 1: Create account \n Press 2: Transaction \n press 3: Show Accounts \n press 4: To exit app \n: ')
    if (accountOptions == "1"):
        createAccount()
    elif (accountOptions == "2"):
        print('TRANSACTION MENU')
        transaction = input(
            'press 1: Check Balance \n press 2: Withdraw \n press 3: Deposit \n press 4: Transfer  \n press any key to go to main menu \n:')
        if(transaction == '1'):
            checkBalance()
        elif(transaction == '2'):
            withdrawMoney()
        elif(transaction == '3'):
            depositMoney()
        elif(transaction == '4'):
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
    print('WITHDRAW')
    user = input('enter email associated with your account: ')
    if(userExists(user)):
        withdrawal = input('please enter an amount to withdraw: ')
        if(int(withdrawal) > int(userDetails(user)[2])):
            print('your account is too low for withdrawal!!,')
            depositMoney()
        else:
            amountToWithdraw = int(withdrawal)
            totalAmountLeft = int(userDetails(user)[2]) - amountToWithdraw
            if(setNewAmount(totalAmountLeft, user)):
                print('you have withdrawn ' + 'N' + str(withdrawal) +
                      '. You have N' + str(totalAmountLeft)+' left')
            startAccount()
    else:
        createAccount()


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
    print('TRANSFER')
    user = input('enter email associated with your account: ')
    if(userExists(user)):
        transfer = input('please enter an amount to transfer: ')
        if(userDetails(user)[2] >= int(transfer)):
            if(setNewAmount(transfer, user)):
                print('Transfer of N' + transfer + ' successful!')
                startAccount()
        else:
            print('You cannot transfer this amount!!, try depositing and transfer again!')
            depositMoney()


def depositMoney():
    print('DEPOSIT')
    user = input('enter email associated with your account: ')
    if(userExists(user)):
        deposit = input('please enter an amount to deposit: ')
        if(int(deposit) > userDetails(user)[2]):
            if(setNewAmount(deposit, user)):
                print('Deposit successful!!')
                startAccount()
        else:
            print('You cannot deposit this amount!!')
            startAccount()
    else:
        createAccount()


def checkBalance():
    user = input('please enter your email associated with account: ')
    if(userExists(user)):
        print("You have a total of" + " N" + str(userDetails(user)[2]) + '\n')
        startAccount()
    else:
        createAccount()


def validateAccount(email, password):
    if(email == "" or password == ""):
        print('email and password cannot be empty!!')
        createAccount()
    for i in userAccounts:
        if i['email'] == email:
            print('email already exists...')
            createAccount()
        elif i['password'] == password:
            print('password already exists...')
            createAccount()
    return True


def createAccount():
    print('NEW ACCOUNT')
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
