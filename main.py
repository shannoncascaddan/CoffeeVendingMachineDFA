#take in input string through commandline
inputString = ""
print("Welcome to the Coffee Vending Machine")
inputString += input("Please select coffee type (a = black, b = cold brew, c = espresso):")
inputString += input("Please select cup size (a = Small, b = Medium, c = Large):")
inputString += input("Please select your customizations (a = cream, b = sugar, c = cream and sugar):")
inputString += input("Please select your payment type (a = cash, b = card, c = E-wallet):")
inputString += input("Press 'a' to dispense: ")
print(inputString)


#Setup DFA
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
    'payment_Processed': {'a': 'coffee_Dispensed'},
    'error_Detected': {'customization_Complete'},
    'coffee_Dispensed': {'idle'}
}

options = {
    'idle': {'a': 'Black Coffee', 'b': 'Cold Brew', 'c': 'Espresso'},
    'coffee_Selected': {'a': 'Small', 'b': 'Medium', 'c': 'Large'},
    'cup_Size_Selected': {'a': 'Cream', 'b': 'Sugar', 'c': 'Cream and Sugar'},
    'customization_Complete': {'a': 'Cash', 'b': 'Card', 'c': 'E-Wallet'},
    'payment_Processed': {'a': 'coffee_Dispensed'},
    'error_Detected':{'customization_Complete'},
    'coffee_Dispensed': {'idle'}
}
#test if accepted states or not
currState = startState
print("Start State: " + currState)
for char in inputString:
    if char not in alphabet:
        print("Invalid Input")
        currState = 'error_Detected'
        inChar = input("Please select a valid input for " + currState)

    else:
        currState = transition[currState][char]
        print(char + " --> " + currState)

#Output order
print("Thank you!")
print("Order Details:")
print("Coffee Dispensed")

