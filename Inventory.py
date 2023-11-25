import sqlite3
import sys

try:
    connection = sqlite3.connect("Inventory.db")
    print("Successfull connection.")

except:
    print("Failed connection.")
    sys.exit()

    
class Inventory:
    def __init__(self):
        self

    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName
    
    def viewInventory():
        cursor = connection.cursor()
        print()
        cursor.execute("SELECT * FROM Inventory")
        result = cursor.fetchall()
        for x in result:
            print("ISBN:", x[0], "\tTitle:", x[1], "\tAuthor:", x[2], "\tGenre:", x[3], "\tPages:", x[4], "\tRelease Date:", x[5], "\tStock:", x[6])
            print("\n\n")
        cursor.close()
        connection.close()

    def searchInventory(Search):
        cursor = connection.cursor()
        print()
        cursor.exectute("SELECT * FROM Inventory WHERE Title=Search")
        result = cursor.fetchall()
        for x in result:
            print("ISBN:", x[0], "\tTitle:", x[1], "\tAuthor:", x[2], "\tGenre:", x[3], "\tPages:", x[4], "\tRelease Date:", x[5], "\tStock:", x[6])
            print("\n\n")
        cursor.close()
        connection.close()

    def decreaseStock(decISBN):
        cursor = connection.cursor()
        print()
        cursor.execute("UPDATE Inventory SET Stock WHERE ISBN=decISBN")    ##not complete
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
