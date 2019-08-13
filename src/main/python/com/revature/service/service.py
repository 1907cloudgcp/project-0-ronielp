import controller.controller as controller
import IO.users as users

class Service:
    def __init__(self):
        self.state = 'first'
        self.Controller = controller.Controller(self)
        self.Controller.run()

    def register(self, inName, inPassword):
        self.User = users.User(self, inName, inPassword)
        #input()