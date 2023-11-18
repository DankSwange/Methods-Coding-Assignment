class Cart:
    databaseName = ''
    tableName = ''

    def __init__(self):
        self.databaseName = 'N/A'
        self.tableName = 'N/A'
    
    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName

    def viewCart(userID, inventoryDatabase)
    
    def addToCart(userID, ISBN)
    
    def removeFromCart(userID, ISBN)
        
    def checkOut(userID)
