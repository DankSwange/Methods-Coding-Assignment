import User
import Inventory
import Cart

use = User("Design.db", "User")

def mainMenu(use):
  print("Welcome, {use.firstName}/n/n")
  print("Please choose an option")
  print("1. Logout/n")
  print("2. View Account Information/n")
  print("3. Access Inventory Information/n")
  print("4. Access Cart Information/n")
  MMOption = input()
  while (MMOption > 0 and MMOption < 5):
    if (MMOption == 1):
      use.logout()
    else if (MMOption == 2):
      use.viewAccountInformation()
    else if (MMOption == 3):
      inventoryMenu(use)
    else if (MMOption == 4):
      cartMenu(use)

def inventoryMenu(use):
  print("Welcome to the Inventory menu, please choose an option to get started!")
  inventoryOption = 0
  while (inventoryOption != 1):
    print("1. Go back\n")
    print("2. View Inventory\n")
    print("3. Search Inventory\n")
    inventoryOption = input("Please select a valid option from the menu above 1-3: ")
    while (inventoryOption > 0 and inventoryOption < 4):
      if (inventoryOption == 2):
        inven = Inventory("Design.db", "Inventory")
        inven.viewInventory()

      if (inventoryOption == 3):
        inven = Inventory("Design.db", "Inventory")
        title = input("Enter the name of the book you would like to search for: ")
        inven.searchInventory(title)
    
def cartMenu(use):
    while (True):
        inventory = Inventory("Design.db", "Inventory")
        cart = Cart("Design.db", "Cart")
        userChoice = 0

        print("1. Go back\n2. View cart\n3. Add item to cart\n4. Remove item from cart\n5. Check out\n")

        while (userChoice < 1 and userChoice > 5):
            userChoice = input("What would you like to do? (Enter a choice 1-5): ")
    
        if (userChoice == 1):
            break
        elif(userChoice == 2):
            cart.viewCart(use.getUserID, "Inventory")
        elif(userChoice == 3):
            inventory.viewInventory()
            item = input("Enter item to add to cart: ")
            cart.addToCart(user.getUserID, item)
        elif(userChoice == 4):
            ISBN = input("Enter the item to be removed: ")
            cart.removeFromCart(use.getUserID, ISBN)
        elif(userChoice == 5):
            cart.checkOut(use.getUserID)
        

print("Welcome to our Store, please choose an option to get started!")
option = 0
while (option > 0 and option < 4):
  print("1. Login/n")
  print("2. Create Account/n")
  print("3. Logout/n")
  option = input("Choose a number: ")
  if(option == 1):
    email = input("Enter your email: ")
    print()
    password = input("Enter your password: ")
    use.login(email, password)
    if(use.loggedIn == True):
      mainMenu(use)
  else if(option == 2):
    use.createAccount()
    mainMenu(use)
  else if (option == 3):
    use.logout()

