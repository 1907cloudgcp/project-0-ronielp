import controller.controller as controller
import IO.users as users

class Service:
    def __init__(self):
        # Initialize the service layer and run the console.
        self.state = 'first'
        self.console = controller.Controller(self)
        self.console.run()

    def register(self, inName, inPassword):
        # Add the user with new name and password to user list.
        users.userList.append(users.User(inName, inPassword))
        # Add the registration to user's transaction list.
        newTransaction = 'User ' + inName + ' registered, Inital Balance: $0'
        users.userList[users.currentUser].addTransaction(newTransaction)

    def login(self, inName, inPassword):
        index = 0
        # Parse through the user list and find the matching user and password.
        for i in users.userList:
            if i.getName() == inName and i.getPassword() == inPassword:
                users.currentUser = index
                print('Login Success!')
                print('--------------------')
                self.state = 'second'
            index += 1

    def viewBalance(self):
        print('Current Balance: $' + str(users.userList[users.currentUser].getBalance()))
        print('--------------------')

    def withdraw(self, withdrawal):
        # First make sure the funds are sufficient for the withdrawal.
        if withdrawal > users.userList[users.currentUser].getBalance():
            print('ERROR: Insufficient funds! Withdrawl amount exceeds balance.')
            print('--------------------')
        else:
            # Get the balance and subtract from it the withdrawal amount.
            newBalance = users.userList[users.currentUser].getBalance()
            newBalance -= withdrawal
            users.userList[users.currentUser].setBalance(newBalance)
            # Add this withdrawal to the transaction list.
            newTransaction = 'Withdrew $' + str(withdrawal) + ', New Balance: $' + str(newBalance)
            users.userList[users.currentUser].addTransaction(newTransaction)
            print('New Balance: $' + str(users.userList[users.currentUser].getBalance()))
            print('--------------------')

    def deposit(self, cash):
        # Add the deposit to the current cash balance.
        newBalance = users.userList[users.currentUser].getBalance()
        newBalance += cash
        users.userList[users.currentUser].setBalance(newBalance)
        # Add this deposit to transaction list.
        newTransaction = 'Deposited $' + str(cash) + ', New Balance: $' + str(newBalance)
        users.userList[users.currentUser].addTransaction(newTransaction)
        print('New Balance: $' + str(users.userList[users.currentUser].getBalance()))
        print('--------------------')

    def viewTransactions(self):
        print('--------------------')
        print('Transactions for ' + users.userList[users.currentUser].getName())
        for elem in users.userList[users.currentUser].getTransactions():
            print(elem)
        print('--------------------')

    def logout(self):
        print('--------------------')
        self.state = 'first'

