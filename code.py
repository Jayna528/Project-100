atmint = 0
atmsafety = 0
transactions = 0
deposits = 0
withdrawl = 0


pin = 1234
creditcardnumber = 1213

enterCCnumber = int(input('Enter your credit card number here --> '))
print(enterCCnumber)

while(atmsafety == 0):
    if(enterCCnumber == creditcardnumber):
        enterpin = int(input('enter your pin number here --> '))
        if(enterpin == pin):
            atmsafety = 1
            print('Your bank account is now unlocked ')
        else: 
            errorpin = int(input('Your pin was entered incorrectly please re-enter your pin number --> '))
            if(errorpin == pin):
                atmsafety = 1
                print('Your bank account is now unlocked' )
            else:
                errorpin = int(input('Your pin was entered incorrectly please re-enter your pin number --> '))
            
    else:
        errorCCnumber = int(input('Your credit card number was incorrect please re-enter your creditcard number '))
        if(errorCCnumber == creditcardnumber):
            enterpin = int(input('enter your pin number here --> '))
        else:
            errorCCnumber = int(input('Your credit card number was incorrect please re-enter your creditcard number '))




if(atmsafety == 1):
    transactions = 3    

while(transactions > 0):
    methods = input('Would you like to make a deposit(d), a withdrawal(w), or sign out(s)? ')

    if(methods == 'd'): 
        deposits = float(input('How much money do you wish to depsoit into your bank account? Please enter in numerical form. '))
        atmint = atmint + deposits 
        print('Your bank account is now worth', atmint, 'dollars ')
        transactions = transactions - 1

    elif(methods == 'w'):
        withdrawals = float(input('How much money do you wish to withdraw from your bank account? Please enter in numerical form. '))
        if(atmint - withdrawals >= 0):
            atmint = atmint - withdrawals
            transactions = transactions - 1
        else:
            print("We are unable to process this request as your bankaccount holds insufficient fundings.")
        print('Your bank account is now worth', atmint, 'dollars')

    elif(methods == 's'):
        print('Thank you for using DUMPYS BANK ACCOUNT! we hope to see you soon.')
        transactions = transactions - 3

    if(transactions <= 0):
        print("Thank you for using DUMPY'S BANK ACCOUNT! we hope to see you soon.")
    
    
    

    
        







    

