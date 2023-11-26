import sqlite3
import sys

try:
    connection = sqlite3.connect("Inventory.db")

except:
    print("Failed connection.")

    sys.exit()

cursor = connection.cursor()



class Cart:
    databaseName = ''
    tableName = ''

    def __init__(self):
        self.databaseName = 'N/A'
        self.tableName = 'N/A'
    
    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName

    def viewCart(self, userID, inventoryDatabase):
        query = "SELECT * FROM ? WHERE ISBN IN (SELECT ISBN FROM Cart WHERE userID=?)"
        data = (inventoryDatabase, userID)  # this could cause an error
        cursor.execute(query, data)

        result = cursor.fetchall()

        print("Your cart contents: \n")

        for x in result:
            Print() #FINISH

    def addToCart(self, userID, ISBN):
        return

    def removeFromCart(self, userID, ISBN):
        return
    
    def checkOut(self, userID):
        return
