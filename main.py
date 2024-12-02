# take in input string through commandline
inputString = ""
orderDetails = ""
total = 0
payment = ""

print("Welcome to the Coffee Vending Machine")
inputString += input("Please select coffee type (a = black, b = cold brew, c = espresso):")
inputString += input("Please select cup size (a = Small($3), b = Medium($4), c = Large($5)):")
inputString += input("Please select your customizations (a = cream, b = sugar, c = cream and sugar):")
inputString += input("Please select your payment type (a = cash, b = card, c = E-wallet):")
inputString += input("Press 'a', 'b', or 'c' to dispense: ")
print(inputString)


# Setup DFA
states = ['idle', 'coffee_Selected', 'cup_Size_Selected', 'customization_Complete',
          'payment_Processed', 'coffee_Dispensed', 'error_Detected']
alphabet = ['a', 'b', 'c']
startState = 'idle'
acceptanceState = ['coffee_Dispensed', 'idle']
transition = {
    'idle': {'a': 'coffee_Selected', 'b': 'coffee_Selected', 'c': 'coffee_Selected'},
    'coffee_Selected': {'a': 'cup_Size_Selected', 'b': 'cup_Size_Selected', 'c': 'cup_Size_Selected'},
    'cup_Size_Selected': {'a': 'customization_Complete', 'b': 'customization_Complete', 'c': 'customization_Complete'},
    'customization_Complete': {'a': 'payment_Processed', 'b': 'payment_Processed', 'c': 'payment_Processed'},
    'payment_Processed': {'a': 'coffee_Dispensed', 'b': 'coffee_Dispensed', 'c': 'coffee_Dispensed'},
    'error_Detected': {'customization_Complete'},
    'coffee_Dispensed': {'idle'}
}

# dictionary to store order details options
options = {
    'coffee_Selected': {'a': 'Coffee Type: Black Coffee', 'b': 'Coffee Type: Cold Brew', 'c': 'Coffee Type: Espresso'},
    'cup_Size_Selected': {'a': 'Size: Small($3)', 'b': 'Size: Medium($4)', 'c': 'Size: Large($5)'},
    'customization_Complete': {'a': 'Customization: Cream', 'b': 'Customization: Sugar', 'c': 'Customization: Cream and Sugar'},
    'payment_Processed': {'a': 'Payment Type: Cash', 'b': 'Payment Type: Card', 'c': 'Payment Type: E-Wallet'},
    'coffee_Dispensed': {'a': '', 'b': '', 'c': ''}
}

# dictionary of what to ask for when input is invalid
reenterStr = {'idle': 'coffee type (a = black, b = cold brew, c = espresso)',
              'coffee_Selected': 'cup size (a = Small, b = Medium, c = Large)',
              'cup_Size_Selected': 'your customizations (a = cream, b = sugar, c = cream and sugar)',
              'customization_Complete': 'payment type (a = cash, b = card, c = E-wallet)',
              'payment_Processed': 'dispensing (a, b, or c)'
              }

# test if accepted states or not, move through DFA
currState = startState
print("Start State: " + currState)
for char in inputString:
    inChar = char
    while inChar not in alphabet:  # error handling
        print(inChar + " --> error detected")
        inChar = input("Please select a valid input for " + reenterStr[currState] + ": ")

    # transition DFA states
    currState = transition[currState][inChar]
    orderDetails += '\n' + options[currState][inChar]
    print(inChar + " --> " + currState)

    # set prices based on cup size
    if currState == 'cup_Size_Selected':
        if inChar == 'a':
            total = 3.00
        if inChar == 'b':
            total = 4.00
        if inChar == 'c':
            total = 5.00

    # handle payment
    if currState == 'payment_Processed':
        if inChar == 'a':# cash
            cash = input("Enter amount of cash input: $")
            change = float(cash) - total
            while change < 0:
                cash = input("Insufficient funds. Please enter more cash. New amount of chash input: $ ")
                change = float(cash) - total
            else:
                payment = "Change due: $" + str(change)
        elif inChar == 'b':# card
            payment = "Please insert card \n Payment accepted\n"
        elif inChar == 'c':# E wallet
            payment = "Please tap E-wallet device \n Payment accepted\n"


# check if input is accepted and output order details
if currState in acceptanceState:
    print("\nThank you! \n")
    print("Order Details:" + orderDetails)
    print(payment)
    print("Coffee Dispensed")
