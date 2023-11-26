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
        query = "SELECT * FROM ? WHERE ISBN IN (SELECT ISBN FROM Cart WHERE UserID=?)"
        data = (inventoryDatabase, userID)  # this could cause an error
        cursor.execute(query, data)

        result = cursor.fetchall()

        print("Your cart contents: \n")

        for x in result:
            print("Book:", x[1], "by", x[2])
            print()

    def addToCart(self, userID, ISBN):
        cursor.execute("SELECT * FROM Cart")
        result = cursor.fetchall()

        quantity = 1

        for x in result:
            if x[0] == userID and x[1] == ISBN:
                quantity = quantity + int(x[2])
        
        if quantity > 1:
            query = "UPDATE Cart SET Quantity=? WHERE UserID=? AND ISBN=?"
            data = (quantity, userID, ISBN)
        else:
            query = "INSERT INTO Cart (UserID, ISBN, Quantity) VALUES (?, ?, ?)"
            data = (userID, ISBN, quantity)

        cursor.execute(query, data)
        connection.commit()

        print("Added item to cart.\n")

    def removeFromCart(self, userID, ISBN):
        cursor.execute("SELECT * FROM Cart")
        result = cursor.fetchall()

        quantity = 1

        for x in result:
            if x[0] == userID and x[1] == ISBN:
                quantity = quantity + int(x[2])

        if quantity > 1:
            quantity = quantity - 1

            query = "UPDATE Cart SET Quantity=? WHERE UserID=? AND ISBN=?"
            data = (quantity, userID, ISBN)
        else:
            query = "DELETE FROM Cart WHERE UserID=? AND ISBN=?"
            data = (userID, ISBN)
        
        cursor.execute(query, data)
        connection.commit()

        print("Removed item from cart.\n")

    def checkOut(self, userID):
        query = "SELECT * FROM Cart WHERE UserID=?"
        data = (userID) # This might cause an error
        cursor.execute(query, data)
        result = cursor.fetchall()
        
        for x in result:
            if x[2] > 1:
                for x in range[x[2]]:
                    decreaseStock(x[1])
            else:
                decreaseStock(x[1])
                
        query = "DELETE FROM Cart WHERE UserID=?"
        data = (userID,)

        cursor.execute(query,data)
        connection.commit()

        print("You have successfully checked out.\n")

cursor.close()
connection.close()
