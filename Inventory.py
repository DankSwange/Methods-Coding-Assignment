import sqlite3
import sys

    
class Inventory:
    def __init__(self):
        self

    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName
        try:
            connection = sqlite3.connect("databaseName")
            print("Successful connection.")

        except:
            print("Failed connection.")
            sys.exit()
    
    def viewInventory():
        cursor = connection.cursor()
        print()
        cursor.execute("SELECT * FROM tableName")
        result = cursor.fetchall()
        for x in result:
            print("ISBN:", x[0], "\tTitle:", x[1], "\tAuthor:", x[2], "\tGenre:", x[3], "\tPages:", x[4], "\tRelease Date:", x[5], "\tStock:", x[6])
            print("\n\n")
        cursor.close()
        connection.close()

    def searchInventory(search):
        cursor = connection.cursor()
        print()
        cursor.exectute("SELECT * FROM tableName WHERE Title=search") ## need to ask how to check if failure
        result = cursor.fetchall()
        for x in result:
            if (x == 0):
                print("Search failed: book is not in inventory.\n)
            else:
                print("ISBN:", x[0], "\tTitle:", x[1], "\tAuthor:", x[2], "\tGenre:", x[3], "\tPages:", x[4], "\tRelease Date:", x[5], "\tStock:", x[6])
                print("\n\n")
        cursor.close()
        connection.close()

    def decreaseStock(decISBN, quantityBought):
        cursor = connection.cursor()
        print()
        dec = cursor.exectute("SELECT Stock FROM tableName WHERE ISBN=decISBN")  ##dec is created to deincrement the stock
        dec -= quantityBought
        cursor.execute("UPDATE tableName SET Stock=dec WHERE ISBN=decISBN")
        connection.commit()
        cursor.close()
        connection.close()

    def getDatabaseName(self):
        return self.databaseName
    
    def getTableName(self):
        return self.tableName
    
    def setDatabaseName(self, databaseName):
        self.databaseName = databaseName

    def setTableName(self, tableName):
        self.tableName = tableName
