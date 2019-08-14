#import sys
import logging

class Controller:
    def __init__(self, inService):
        logging.info('New bank session began')
        print('Welcome to the Bank of Padua!')
        print('--------------------')
        self.service = inService

    # Main console runs from here.
    def run(self):
        while True:
            # If the state is first, then a user is not logged in.
            if self.service.state == 'first':
                print('Please register an account or login to an existing one.')
                print('(1) Register')
                print('(2) Login')
                print('(3) Exit Program')
                choice = input('    Input: ')
                if choice == '1':
                    print('--------------------')
                    inputName = input('Please enter your name: ')
                    inputPass = input('Please enter a password for your account: ')
                    self.service.register(inputName, inputPass)
                elif choice == '2':
                    loginName = input('Please enter your name: ')
                    loginPass = input('Please enter your password: ')
                    self.service.login(loginName, loginPass)
                elif choice == '3':
                    logging.info('Banking session ended')
                    quit()
                else:
                    print('Invalid option')

            # A state of second indicates a user is logged in.
            elif self.service.state == 'second':
                print('Please select an action:')
                print('(1) View Balance')
                print('(2) Withdraw Money')
                print('(3) Deposit Money')
                print('(4) View Past Transactions')
                print('(5) Logout')
                choice = input('    Input: ')
                if choice == '1':
                    self.service.viewBalance()
                elif choice == '2':
                    withdrawalAmount = input("Amount you'd like to withdraw: ")
                    try:
                        withdrawal = float(withdrawalAmount)
                        self.service.withdraw(abs(withdrawal))
                    # Handling error of non-integer input from user.
                    except ValueError:
                        logging.error('Withdrawal input was not a number')
                        print('Input was not a numerical value.')
                        print('--------------------')
                elif choice == '3':
                    depositInput = input("Amount you'd like to deposit: ")
                    try:
                        depositAmount = float(depositInput)
                        self.service.deposit(abs(depositAmount))
                    # Handling error of non-integer input from user.
                    except ValueError:
                        logging.error('Deposit input was not a number')
                        print('Input was not a numerical value.')
                        print('--------------------')
                        pass
                elif choice == '4':
                    self.service.viewTransactions()
                elif choice == '5':
                    self.service.logout()

