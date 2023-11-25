class Users:
    def __init__(self):
        self.userID = None
        self.password = None
        self.firstName = None
        self.lastName = None
        self.address = None
        self.state = None
        self.zip = None
        self.payment = None
        self.loggedIn = False
        self.tableName = None
        self.databaseName = None

    def  User(self, databaseName, tableName):

    def login(self, userID, loggedIn):
        self.loggedIn = True
        
    def logout(self, UserID):
        self.UserID = None
        self.loggedIn = False
    
    def viewAccountInformation(self, UserID):

    def createAccount(self): 
        if self.loggedIn == True:
            print("You are already logged in, please logout to create an account.")
        else:
            self.email = input("Enter your email: ")
            self.password = input("Create a new password: ")
            self.firstName = input("Enter your First Name: ")
            self.lastName = input("Enter your Last name: ")
            self.address = input("Enter your address: ")
            self.state = input("Enter your state: ")
            self.zip = input("Enter your zip: ")
            self.payment = input("Enter your payment type: ")
            self.AccountInformation = {UserID, email, password, firstName, lastName, address, city, state, zip, payment}
            self.loggedIn = True
            print("Account creation successful.")
    
    def getLoggedin(self):
        return self.loggedIn

    def getUserID(self):
        return self.UserID
