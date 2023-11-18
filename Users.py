class Users:
    def __init__(self):
        self.userID = None
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
            self.userID = input("Enter your FirstName-LastName")
            print("Your UserID is {self.userID}.")
            self.loggedIn = True
            print("Account creation successful.")
    
    def getLoggedin(self):
        return self.loggedIn

    def getUserID(self):
        return self.UserID

