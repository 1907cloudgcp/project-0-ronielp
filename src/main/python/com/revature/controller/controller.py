class Controller:
    def __init__(self, Service):
        print('Welcome to the Bank of Padua!')
        self.service = Service

    def run(self):
        while(True):
            if(self.service.state == 'first'):
                print('Please register or login.')
                print('1. Register')
                print('2. Login')
                choice = input()
                if(choice == '1'):
                    inputName = input('Please enter your name: ')
                    inputPass = input('Please enter a password for your account: ')
                    self.service.register(inputName, inputPass)
                elif(choice == '2'):
                    self.service.login()
            elif (self.service.state == 'first'):
                print('inside')
            elif(self.service.state == 'first'):
                print('inside')
            elif(self.service.state == 'first'):
                print('inside')
