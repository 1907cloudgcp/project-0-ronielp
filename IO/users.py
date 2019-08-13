class User:
    def __init__(self, inName='', inPassword='', inBalance=0, inTransactions=[]):
        self.name = inName
        self.password = inPassword
        self.balance = inBalance
        self.transactions = inTransactions

    def setName(self, inName):
        self.name = inName

    def setPassword(self, inPassword):
        self.password = inPassword

    def setBalance(self, inBalance):
        self.balance = inBalance

    def setTransactions(self, inTransactions):
        self.transactions = inTransactions