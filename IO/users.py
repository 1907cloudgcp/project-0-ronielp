class User():
    def __init__(self, inName='', inPassword='', inBalance=0.00, inTransactions=[]):
        self.name = inName
        self.password = inPassword
        self.balance = inBalance
        self.transactions = inTransactions

    def getName(self):
        return self.name

    def getPassword(self):
        return self.password

    def getBalance(self):
        return self.balance

    def getTransactions(self):
        return self.transactions

    def setName(self, inName):
        self.name = inName

    def setPassword(self, inPassword):
        self.password = inPassword

    def setBalance(self, inBalance):
        self.balance = inBalance

    def addTransaction(self, inTransaction):
        self.transactions.append(inTransaction)


userList = []
currentUser = 0