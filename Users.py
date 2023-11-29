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
        self.tableName = ""

    def login(self, email, password, loggedIn):
        self.loggedIn = True
        
    def logout(self, loggedIn):
        if self.loggedIn = True:
            self.userID = ""
            self.loggedIn = False
    
    def viewAccountInformation(self, databaseName, tableName): 
        cursor.execute(f"SELECT * FROM User WHERE UserID={userID}")

        result = cursor.fetchall()

        print("Your account info: \n")

        for x in result:
            print("Name:", x[1], "by", x[2])
            print()

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
            self.AccountInformation = {email, password, firstName, lastName, address, city, state, zip, payment}
            self.loggedIn = True
            cursor.execute("INSERT INTO User (Email, Password, firstName, lastName, Address, City, State, Zip, Payment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)\
            data = (f"{email}, {password}, "{firstName}", "{lastName}", "{lastName}", "{address}", "{state}", "{zip}". "{payment}")
            cursor.execute(query, data)
            connection.commit()
            print("Account creation successful.")
    
    def getLoggedin(self):
        return self.loggedIn

    def getUserID(self):
        return self.UserID

cursor.close()
connection.close()
