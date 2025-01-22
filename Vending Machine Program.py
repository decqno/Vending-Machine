import os

#Variables to be included in the Program
xScreenNo = 0
xMainChoice = 0
xStartRange = 1
xEndRange = 4
xMaxInputRange = 999999999

xCocoaQty = 0
xSugarQty = 0
xMilkQty = 0
xNutsQty = 0

xCocoaAmount = 1
xSugarAmount = 1
xMilkAmount = 1
xNutsAmount = 1

xDarkChocoDefLevelCocoa = 4
xDarkChocoDefLevelSugar = 2
xDarkChocoDefLevelMilk = 1
xDarkChocoDefLevelNuts = 0
xDarkChocoAmount = (xDarkChocoDefLevelCocoa * xCocoaAmount) + (xDarkChocoDefLevelSugar * xSugarAmount) + (xDarkChocoDefLevelMilk * xMilkAmount) + (xDarkChocoDefLevelNuts * xNutsAmount)
xDarkChocoTotalQuantity = 0
xDarkChocoTotalAmount = 0

xWhiteChocoDefLevelCocoa = 1
xWhiteChocoDefLevelSugar = 3
xWhiteChocoDefLevelMilk = 4
xWhiteChocoDefLevelNuts = 0
xWhiteChocoAmount = (xWhiteChocoDefLevelCocoa * xCocoaAmount) + (xWhiteChocoDefLevelSugar * xSugarAmount) + (xWhiteChocoDefLevelMilk * xMilkAmount) + (xWhiteChocoDefLevelNuts * xNutsAmount)
xWhiteChocoTotalQuantity = 0
xWhiteChocoTotalAmount = 0

xStandardChocolateSnickersAmount = 5
xStandardChocolateTwixAmount = 5
xStandardChocolateGalaxyAmount = 5
xStandardChocolateMarsAmount = 5

xStandardChocoSelected = 0
xStandardChocoSelectedName = ""
xStandardChocoTotalQuantity = 0
xStandardChocoTotalAmount = 0

xTotalQuantity = 0
xTotalAmount = 0
xTotalPaidAmount = 0
xTotalChange = 0

#This is the default screen that is always presented throughout the user's vending machine experience
def fScreen(xMessage):
    os.system("cls")

    print("===========================================\n")
    print(xMessage)
    print("\n===========================================\n")
    print("Press M to go back to Main screen.\n")

#This function keeps track of the user's inputs, ensuring its validity.
def fValidInput(xStart, xEnd, xMessage, xErrorMessage):
    while True:
        try:
            xInput = input(xMessage) 
            if str(xInput).lower() == "m":
                fSelectScreen(0)
                break
            else:
                xLevel = int(xInput)
                if int(xStart) <= int(xLevel) <= int(xEnd):
                    return xLevel
                else:
                    print(xErrorMessage)
                    
        except:
            print(xErrorMessage)

#This function leads the user to a certain screen based on their input. (used for the main screen)     
def fSelectScreen(xScreenNo):
    match int(xScreenNo):
        case 1:
            fMakeYourChocoScreen()
        case 2:
            fDarkChocolateScreen()
        case 3:
            fWhiteChocolateScreen()
        case 4:
            fStandardChocolateScreen()
        case _:
            fMainScreen()

#This screen presents the main menu, wherein the user can select what chocolate they wish to have.
def fMainScreen():
    fScreen(
        "Welcome to MixYourChoco Vending Machine!\n"
        "How would you like your chocolate?\n"
        "1 - Make Your Own Chocolate\n"
        "2 - Dark Chocolate\n"
        "3 - White Chocolate\n"
        "4 - Standard Chocolate\n"
        )
    xMainChoice = fValidInput(xStartRange, xEndRange, xMessage = "Select from 1-4: ", xErrorMessage = "Please enter numbers from 1-4 only.")
    fSelectScreen(xMainChoice)

#This function focuses on the whole process of the user making their own chocolate, asking the users preferences and calculating the total amount of bill.
def fMakeYourChocoScreen():
    fScreen(
        "You selected to Make Your Own Chocolate.\n"
        )
    xCocoaQty = fValidInput(xStartRange, xEndRange, xMessage = "Select Cocoa Level from 1-4: ", xErrorMessage = "Please enter numbers from 1-4 only.")
    xMilkQty = fValidInput(xStartRange, xEndRange, xMessage = "Select Milk Level from 1-4: ", xErrorMessage = "Please enter numbers from 1-4 only.")
    xSugarQty = fValidInput(xStartRange, xEndRange, xMessage = "Select Sugar Level from 1-4: ", xErrorMessage = "Please enter numbers from 1-4 only.")
    xNutsQty = fValidInput(xStartRange, xEndRange, xMessage = "Select Nuts Level 1-4: ", xErrorMessage = "Please enter numbers from 1-4 only.")

    xSelfMadeAmount = (xCocoaQty*xCocoaAmount) + (xMilkQty*xMilkAmount) + (xSugarQty*xSugarAmount) + (xNutsQty*xNutsAmount)
    
    fScreen(
        "You selected to Make Your Own Chocolate.\n"
        "Cocoa Amount: " + str(xCocoaQty*xCocoaAmount) + "\n"
        "Milk Amount: " + str(xMilkQty*xMilkAmount) + "\n"
        "Sugar Amount: " + str(xSugarQty*xSugarAmount) + "\n"
        "Nuts Amount: " + str(xNutsQty*xNutsAmount) + "\n"
        "\nOne Self-Made Chocolate costs " + str(xSelfMadeAmount) + " Dhs\n"
        )
    xTotalQuantity = fValidInput(xStartRange, xMaxInputRange, xMessage = "How many would you like to buy?: ", xErrorMessage = "Please enter a correct value.")
    xTotalAmount = xSelfMadeAmount * xTotalQuantity

    fScreen(
        "You selected to Make Your Own Chocolate.\n"
        "Cocoa Amount: " + str(xCocoaQty*xCocoaAmount) + "\n"
        "Milk Amount: " + str(xMilkQty*xMilkAmount) + "\n"
        "Sugar Amount: " + str(xSugarQty*xSugarAmount) + "\n"
        "Nuts Amount: " + str(xNutsQty*xNutsAmount) + "\n"
        "\nTotal Amount: " + str(xTotalAmount) + " Dhs\n"
        )
    xTotalPaidAmount = fValidInput(xTotalAmount, xMaxInputRange, xMessage = "How much will you pay?: ", xErrorMessage = "Please enter a correct value.")
    xTotalChange = xTotalPaidAmount - xTotalAmount

    fScreen(
        "You selected to Make Your Own Chocolate.\n"
        "Cocoa Amount: " + str(xCocoaQty*xCocoaAmount) + "\n"
        "Milk Amount: " + str(xMilkQty*xMilkAmount) + "\n"
        "Sugar Amount: " + str(xSugarQty*xSugarAmount) + "\n"
        "Nuts Amount: " + str(xNutsQty*xNutsAmount) + "\n"
        "\nTotal Amount: " + str(xTotalAmount) + " Dhs\n"
        "Total Paid Amount: " + str(xTotalPaidAmount) + " Dhs\n"
        "Total Change Amount: " + str(xTotalChange) + " Dhs\n"
        )
    
    fValidInput(xStart = "m", xEnd = "m", xMessage = "", xErrorMessage="")

#This function focuses on the dark chocolate's payment process, as its ingredients and price is already set. (refer to the variables at the top)
def fDarkChocolateScreen():
    fScreen(
        "You selected Dark Chocolate.\n"
        "One costs " + str (xDarkChocoAmount) + " Dhs.\n"
        )
    xDarkChocoTotalQuantity = fValidInput(xStartRange, xMaxInputRange, xMessage = "How many would you like to buy?: ", xErrorMessage = "Please enter a correct value.")
    xDarkChocoTotalAmount = xDarkChocoAmount * xDarkChocoTotalQuantity

    fScreen(
        "You selected Dark Chocolate.\n"
        "One costs " + str (xDarkChocoAmount) + " Dhs.\n"
        "\nTotal Quantity: " + str (xDarkChocoTotalQuantity) + "\n"
        "Total Amount: " + str (xDarkChocoTotalAmount) + " Dhs\n"
    )
    xTotalPaidAmount = fValidInput(xDarkChocoTotalAmount, xMaxInputRange, xMessage = "How much will you pay?: ", xErrorMessage = "Please enter a correct value.")
    xTotalChange = xTotalPaidAmount - xDarkChocoTotalAmount

    fScreen(
        "You selected Dark Chocolate.\n"
        "One costs " + str (xDarkChocoAmount) + " Dhs.\n"
        "\nTotal Quantity: " + str (xDarkChocoTotalQuantity) + "\n"
        "Total Amount: " + str (xDarkChocoTotalAmount) + " Dhs\n"
        "Total Paid Amount: " + str (xTotalPaidAmount) + " Dhs\n"
        "Total Change Amount: " + str (xTotalChange) + " Dhs\n"
        )
    
    fValidInput(xStart = "m", xEnd = "m", xMessage = "", xErrorMessage="")

#This function focuses on the white chocolate's payment process, as its ingredients and price is already set. (refer to the variables at the top)
def fWhiteChocolateScreen():
    fScreen(
        "You selected White Chocolate.\n"
        "One costs " + str (xWhiteChocoAmount) + " Dhs.\n"
        )
    xWhiteChocoTotalQuantity = fValidInput(xStartRange, xMaxInputRange, xMessage = "How many would you like to buy?: ", xErrorMessage = "Please enter a correct value.")
    xWhiteChocoTotalAmount = xWhiteChocoAmount * xWhiteChocoTotalQuantity

    fScreen(
        "You selected White Chocolate.\n"
        "One costs " + str (xWhiteChocoAmount) + " Dhs.\n"
        "\nTotal Quantity: " + str (xWhiteChocoTotalQuantity) + "\n"
        "Total Amount: " + str (xWhiteChocoTotalAmount) + " Dhs\n"
    )
    xTotalPaidAmount = fValidInput(xWhiteChocoTotalAmount, xMaxInputRange, xMessage = "How much will you pay?: ", xErrorMessage = "Please enter a correct value.")
    xTotalChange = xTotalPaidAmount - xWhiteChocoTotalAmount

    fScreen(
        "You selected White Chocolate.\n"
        "One costs " + str (xWhiteChocoAmount) + " Dhs.\n"
        "\nTotal Quantity: " + str (xWhiteChocoTotalQuantity) + "\n"
        "Total Amount: " + str (xWhiteChocoTotalAmount) + " Dhs\n"
        "Total Paid Amount: " + str (xTotalPaidAmount) + " Dhs\n"
        "Total Change Amount: " + str (xTotalChange) + " Dhs\n"
        )
    
    fValidInput(xStart = "m", xEnd = "m", xMessage = "", xErrorMessage="")

#This function displays the standard chocolates found in a usual vending machine, and it focuses on the payment process based on the user's selected chocolate.
def fStandardChocolateScreen():
    fScreen(
        "You selected Standard Chocolate.\n"
        "Select Chocolate:\n"
        "1 - Snickers: " + str(xStandardChocolateSnickersAmount) +" Dhs\n"
        "2 - Twix: " + str(xStandardChocolateTwixAmount) +" Dhs\n"
        "3 - Galaxy: " + str(xStandardChocolateGalaxyAmount) +" Dhs\n"
        "4 - Mars: " + str(xStandardChocolateMarsAmount) +" Dhs\n"
        )
    xStandardChocoSelected = fValidInput(xStartRange, xEndRange, xMessage = "Which standard chocolate would you like to buy?: ", xErrorMessage = "Please enter numbers from 1-4 only.")
    xStandardChocoTotalQuantity = fValidInput(xStartRange, xMaxInputRange, xMessage = "How many would you like to buy?: ", xErrorMessage = "Please enter a correct value.")
    match xStandardChocoSelected:
        case 1:
            xStandardChocoTotalAmount = xStandardChocolateSnickersAmount*xStandardChocoTotalQuantity
            xStandardChocoSelectedName = "Snickers"
        case 2:
            xStandardChocoTotalAmount = xStandardChocolateTwixAmount*xStandardChocoTotalQuantity
            xStandardChocoSelectedName = "Twix"
        case 3:
            xStandardChocoTotalAmount = xStandardChocolateGalaxyAmount*xStandardChocoTotalQuantity
            xStandardChocoSelectedName = "Galaxy"
        case 4:
            xStandardChocoTotalAmount = xStandardChocolateMarsAmount*xStandardChocoTotalQuantity 
            xStandardChocoSelectedName = "Mars"
    
    fScreen(
        "You selected Standard Chocolate.\n"
        "Selected Chocolate: "+xStandardChocoSelectedName+"\n"
        "\nTotal Quantity: "+str(xStandardChocoTotalQuantity)+"\n"
        "Total Amount: "+str(xStandardChocoTotalAmount)+" Dhs\n"
        )
    xTotalPaidAmount = fValidInput(xStandardChocoTotalAmount, xMaxInputRange, xMessage = "How much will you pay?: ", xErrorMessage = "Please enter a correct value.")
    xTotalChange = xTotalPaidAmount - xStandardChocoTotalAmount
    
    fScreen(
        "You selected Standard Chocolate.\n"
        "Selected Chocolate: " + (xStandardChocoSelectedName) + "\n"
        "\nTotal Quantity: " + str (xStandardChocoTotalQuantity) + "\n"
        "Total Amount: " + str (xStandardChocoTotalAmount) + " Dhs\n"
        "Total Paid Amount: " + str (xTotalPaidAmount) + " Dhs\n"
        "Total Change Amount: " + str (xTotalChange) + " Dhs\n"
        )
    
    fValidInput(xStart = "m", xEnd = "m", xMessage = "", xErrorMessage="")

fSelectScreen(xScreenNo)