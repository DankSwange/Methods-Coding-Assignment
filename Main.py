inventoryOption = 0
while (inventoryOption != 1):
  print("1. Go back\n")
  print("2. View Inventory\n")
  print("3. Search Inventory\n")
  inventoryOption = input("Please select a valid option from the menu above 1-3: ")
  while (inventoryOption < 1 and inventoryOption > 3):
    inventoryOption = input("Please select a valid option from the menu above 1-3: ")

  
