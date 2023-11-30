import sqlite3
import sys

try:
    connection = sqlite3.connect("Design.db")

except:
    print("Failed connection.")
    sys.exit()

print()

cursor = connection.cursor()

class Users:
    def __init__(self):
        self.userID = ""
        self.password = ""
        self.firstName = ""
        self.lastName = ""
        self.address = ""
        self.state = ""
        self.zip = ""
        self.payment = ""
        self.tableName = ""
        self.databaseName = ""
        self.loggedIn = False

    def  User(self, databaseName, tableName):
        self.databaseName = design.db
        self.tableName = User

    def login(self, email, password, loggedIn):
        self.loggedIn = True
        
    def logout(self, loggedIn):
        if self.loggedIn == True:
            self.userID = ""
            self.loggedIn = False
            return self.loggedIn

        else:
            print("You must be logged in to logout.")
            return
    
    def viewAccountInformation(self, databaseName, tableName): 
        cursor.execute(f"SELECT * FROM User WHERE UserID={userID}")

        result = cursor.fetchall()

        print("Your account info: \n")

        for x in result:
            print(f"Name: {x[3]} {x[4]} /nEmail: {x[1]} /nPassword: {x[2]} /nAddress: {x[5]} /nState: {x[6]} /nZip{x[7]} /nPayment: x[8]")
            print()

        return

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
            self.loggedIn = True
            query = "INSERT INTO User (Email, Password, firstName, lastName, Address, City, State, Zip, Payment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
            data = (f"{email}", f"{password}", f"{firstName}", f"{lastName}", f"{lastName}", f"{address}", f"{state}", f"{zip}", f"{payment}")
            cursor.execute(query, data)
            connection.commit()
            print("Account creation successful.")
            return self.loggedIn
    
    def getLoggedin(self):
        return self.loggedIn

    def getUserID(self):
        return self.UserID

cursor.close()
connection.close()
