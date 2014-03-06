# Financial application: monetary units
# Author: Brian Hamburg

# Get the amount from the user
amount = eval(input("Enter an amount, for example 99.99: "))

# Convert to cents
remainingAmount = int(amount * 100)

# Find the dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# Find the quarters
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

# Find the dimes
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

# Find the nickels
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

# Find the pennies
numberOfPennies = remainingAmount

# Define plurality
dollarName = "dollars"
quarterName = "quarters"
dimeName = "dimes"
nickelName = "nickels"
pennyName = "pennies"

if numberOfOneDollars == 1:
    dollarName = "dollar"
if numberOfQuarters == 1:
    quarterName = "quarter"
if numberOfDimes == 1:
    dimeName = "dime"
if numberOfNickels == 1:
    nickelName = "nickel"
if numberOfPennies == 1:
    pennyName = "penny"

# Display results
print ("Your amount of", amount, "consists of\n",
    "\t", numberOfOneDollars, dollarName, "\n",
    "\t", numberOfQuarters, quarterName, "\n",
    "\t", numberOfDimes, dimeName, "\n",
    "\t", numberOfNickels, nickelName, "\n",
    "\t", numberOfPennies, pennyName)

