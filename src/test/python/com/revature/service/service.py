import controller.controller as controller
import IO.users as users
import logging

class Service:
    def __init__(self):
        # Initialize the service layer and run the console.
        self.state = 'first'
        self.console = controller.Controller(self)
        self.console.run()

    # Registers a user using an input name and password.
    def register(self, inName, inPassword):
        existing = False
        # Parse through the user list and see first if username already exists..
        for i in users.userList:
            if i.getName() == inName:
                print('User already exists! Please register a different name!')
                print('--------------------')
                existing = True
        if not existing:
            # Add the user with new name and password to user list.
            users.userList.append(users.User(inName, inPassword))
            logging.info('New user ' + inName + ' added.')
            # Add the registration to user's transaction list.
            newTransaction = 'User ' + inName + ' registered, Inital Balance: $0'
            users.userList[users.currentUser].addTransaction(newTransaction)

    # Logs user in by comparing input name and password to user list.
    def login(self, inName, inPassword):
        index = 0
        found = False
        # Parse through the user list and find the matching user and password.
        for i in users.userList:
            if i.getName() == inName and i.getPassword() == inPassword:
                logging.debug('Logged in as ' + i.getName() + '.')
                users.currentUser = index
                print('--------------------')
                print('Login Success!')
                print('--------------------')
                found = True
                self.state = 'second'
            index += 1
        if not found:
            print('--------------------')
            print('User and/or password not found.')
            print('--------------------')

    # Prints the current balance of the user.
    def viewBalance(self):
        print('--------------------')
        print('Current Balance: $' + str(users.userList[users.currentUser].getBalance()))
        print('--------------------')

    # Subtracts input withdrawal amount from user's balance.
    def withdraw(self, withdrawal):
        # First make sure the funds are sufficient for the withdrawal.
        if withdrawal > users.userList[users.currentUser].getBalance():
            print('--------------------')
            print('ERROR: Insufficient funds! Withdrawl amount exceeds balance.')
            print('--------------------')
        else:
            # Get the balance and subtract from it the withdrawal amount.
            newBalance = users.userList[users.currentUser].getBalance()
            newBalance -= withdrawal
            users.userList[users.currentUser].setBalance(newBalance)
            logging.info('User withdrew $' + str(withdrawal))
            # Add this withdrawal to the transaction list.
            newTransaction = 'Withdrew $' + str(withdrawal) + ', New Balance: $' + str(newBalance)
            users.userList[users.currentUser].addTransaction(newTransaction)
            print('--------------------')
            print('New Balance: $' + str(users.userList[users.currentUser].getBalance()))
            print('--------------------')

    # Adds input deposit amount to user's balance.
    def deposit(self, cash):
        # Add the deposit to the current cash balance.
        newBalance = users.userList[users.currentUser].getBalance()
        newBalance += cash
        users.userList[users.currentUser].setBalance(newBalance)
        logging.info('User deposited $' + str(cash))
        # Add this deposit to transaction list.
        newTransaction = 'Deposited $' + str(cash) + ', New Balance: $' + str(newBalance)
        users.userList[users.currentUser].addTransaction(newTransaction)
        print('--------------------')
        print('New Balance: $' + str(users.userList[users.currentUser].getBalance()))
        print('--------------------')

    # Views the transactions of the current user using their transaction list.
    def viewTransactions(self):
        print('--------------------')
        print('Transactions for ' + users.userList[users.currentUser].getName())
        for elem in users.userList[users.currentUser].getTransactions():
            print(elem)
        print('--------------------')

    # Logs current user out.
    def logout(self):
        print('--------------------')
        logging.debug('User ' + users.userList[users.currentUser].getName() + ' logged out.')
        self.state = 'first'

