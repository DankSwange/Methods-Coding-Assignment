inventoryOption = 0
while (inventoryOption != 1):
  print("1. Go back\n")
  print("2. View Inventory\n")
  print("3. Search Inventory\n")
  inventoryOption = input("Please select a valid option from the menu above 1-3: ")
  while (inventoryOption < 1 and inventoryOption > 3):
    inventoryOption = input("Please select a valid option from the menu above 1-3: ")

  if (inventoryOption == 2):
    inven = Inventory("Design.db", "Inventory")
    inven.viewInventory()

  if (inventoryOption == 3):
    inven = Inventory("Design.db", "Inventory")
    title = input("Enter the name of the book you would like to search for: ")
    inven.searchInventory(title)
