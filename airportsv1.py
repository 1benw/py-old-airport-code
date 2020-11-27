import csv
import time

airports = []

# Read the CSV File
csv_file = csv.reader(open("Airports.csv"))
for row in csv_file:
    if row != []:
        airports.append(row)

print(airports)


mainMenu = False

mainMenuError = "Error In Option Selection"
mainMenuOptions = [
    { "selector": "1: Enter Airport Details", "function": "enterAirportDetails()" },
    { "selector": "2: Enter Flight Details", "function": "enterFlightDetails()" },
    { "selector": "3: Enter Price Plan and Calculate Profit", "function": "calculatePriceProfit()" },
    { "selector": "4: Clear Data", "function": "clearData()" },
    { "selector": "5: Quit", "function": "quitFlights()" }
]

aircraftTypes = [
    { "name": "Medium Narrow Body", "maxRange": 2650, "standardCapacity": 180, "costPerSeatPer100": 8, "minFirstClass": 8 }, 
    { "name": "Large Narrow Body", "maxRange": 5600, "standardCapacity": 220, "costPerSeatPer100": 7, "minFirstClass": 10 },
    { "name": "Medium Wide Body", "maxRange": 4050, "standardCapacity": 406, "costPerSeatPer100": 5, "minFirstClass": 14 } 
]

currentUKDepartureAirport = False
currentTargetAirport = False
currentAircraftType = False

currentAircraftFirstSeats = False
currentAircraftStandardSeats = False

enteringAirportDetails = False
enteringOtherAirportDetails = False

def quitFlights():
    print("\nThanks For Using the Flight Planner, Goodbye")
    exit()

def clearData():
    ## using "global" keyword So Variables Out of this function can be edited (https://www.geeksforgeeks.org/global-keyword-in-python/)
    global currentAircraftFirstSeats 
    global currentAircraftStandardSeats 
    global currentUKDepartureAirport
    global currentTargetAirport
    global currentAircraftType 

    currentAircraftFirstSeats = False
    currentAircraftStandardSeats = False  
    currentUKDepartureAirport = False
    currentTargetAirport = False
    currentAircraftType = False  
    print("Cleared All Data")
    openMainMenu()

def enterAirportDetails():
    enteringAirportDetails = True
    enteringOtherAirportDetails = False
    while enteringAirportDetails:
        print("Available UK Departure Airports:\nLPL - Liverpool John Lennon\nBOH - Bournemouth International")
        airport = input("\nPlease Select a UK Airport to Depart From: ")
        global currentUKDepartureAirport ## So Variables Out of this function can be edited (https://www.geeksforgeeks.org/global-keyword-in-python/)
        if airport == "LPL":
            currentUKDepartureAirport = "LPL"
            print("Selected LPL - Liverpool John Lennon as UK Departure Airport.")
            enteringAirportDetails = False
            enteringOtherAirportDetails = True
        elif airport == "BOH":
            currentUKDepartureAirport = "BOH"
            print("Selected BOH - Bournemouth International as UK Departure Airport.")
            enteringAirportDetails = False
            enteringOtherAirportDetails = True
        else:
            print('\nInvalid UK Departure Airport!\n')
    while enteringOtherAirportDetails:
        print('\nAvailable Target Airports:\n')
        airportCodes = []
        for airport in airports:
            airportCodes.append(airport[0])
            print(airport[0] + " - " + airport[1])
    
        target = input("\nPlease Select Target Airport: ") 
        try:
            targetSelection = airportCodes.index(target)
            global currentTargetAirport ## So Variables Out of this function can be edited (https://www.geeksforgeeks.org/global-keyword-in-python/)
            currentTargetAirport = target
            print("Selected Target Airport: " + airports[targetSelection][1])
            enteringOtherAirportDetails = False
            openMainMenu()
        except ValueError:
            print("Not a Valid Target Airport Code")


def enterFlightDetails():
    enteringFlightDetails = True
    while enteringFlightDetails:
        aircraftTypesAmount = len(aircraftTypes)
        print("Aircraft Types: \n")
        for index, aircraftType in enumerate(aircraftTypes): # use enumerate to get the index also
            print(index + 1, "-", aircraftType["name"], "-", "Max Flight Range: "+ str(aircraftType["maxRange"]) +",", "Standard Capacity: "+ str(aircraftType["standardCapacity"])+",", "Cost Per Seat Per 100km: "+ str(aircraftType["costPerSeatPer100"]))
        try:
            selectedAircraftTypeNum = int(input("Please Select an Aircraft Option (1-"+str(aircraftTypesAmount)+"): ")) - 1 # take one so it is indexable for the array
            #if (selectedAircraftTypeNum > 0aircraftTypesAmount)
            if (selectedAircraftTypeNum > -1 and selectedAircraftTypeNum < aircraftTypesAmount):
                global currentAircraftType
                currentAircraftType = aircraftTypes[selectedAircraftTypeNum]
                enteringFlightDetails = False
                print('Selected Aircraft Type:', currentAircraftType["name"], "- Max Flight Range: "+ str(currentAircraftType["maxRange"]) +", Standard Capacity: "+ str(currentAircraftType["standardCapacity"])+", Cost Per Seat Per 100km: "+ str(currentAircraftType["costPerSeatPer100"]) + ", Min. First Class Seats: "+str(currentAircraftType["minFirstClass"]))
            else:
                print("Invalid Aircraft Type Selection")
        except ValueError:
            print("You have to input a number")
    print("now here")
    enteringFlightDetails = True
    while enteringFlightDetails:
        standardAmount = currentAircraftType["standardCapacity"]
        minAmount = currentAircraftType["minFirstClass"]
        maxAmount = int(standardAmount / 2)
        try: 
            firstClassSeatAmount = int(input("How Many First Class Seats? (Between "+str(minAmount) +" and "+ str(maxAmount)+"): "))
            if firstClassSeatAmount >= minAmount and firstClassSeatAmount <= maxAmount: 
                print(firstClassSeatAmount)
                global currentAircraftFirstSeats
                global currentAircraftStandardSeats 
                currentAircraftFirstSeats = firstClassSeatAmount
                currentAircraftStandardSeats = (standardAmount - (currentAircraftFirstSeats * 2))
                print(currentAircraftFirstSeats, currentAircraftStandardSeats)
                enteringFlightDetails = False
            else:
                print("The number has to be between "+str(minAmount) +" and "+ str(maxAmount))
        except ValueError: 
            print("You have to input a number")
    openMainMenu()

def calculatePriceProfit():
    if not currentUKDepartureAirport or not currentTargetAirport:
        print("\nYou Have Not Set the Departure or Destination Airports")
        openMainMenu()
    elif not currentAircraftType or not currentAircraftFirstSeats or not currentAircraftStandardSeats:
        print("\nYou Have Not Set the Aircraft Type or Amount of Seats")
        openMainMenu()
    else:
        print('good to go')

def openMainMenu():
    mainMenu = True
    while mainMenu:
        print("\n-------------------------\nFlight Planning Main Menu\n-------------------------")
        if currentUKDepartureAirport and currentTargetAirport:
            print("Selected Airports: ")
            print("Current UK Departure Airport: ", currentUKDepartureAirport)
            print("Current Destination Airport: ", currentTargetAirport)
            print("-------------------------")
        if currentAircraftType and currentAircraftFirstSeats and currentAircraftStandardSeats:
            print("Selected Aircraft: ")
            print('Selected Aircraft Type:', currentAircraftType["name"], "- Max Flight Range: "+ str(currentAircraftType["maxRange"]) +", Cost Per Seat Per 100km: "+ str(currentAircraftType["costPerSeatPer100"]))
            print("Standard Class Seats:", currentAircraftStandardSeats)
            print("First Class Seats:", currentAircraftFirstSeats)
            print("-------------------------")
        for option in mainMenuOptions:  
            print(option["selector"])
        try: 
            selection = int(input("\nPlease Select an Option (1-5): "))
            try:
                eval(mainMenuOptions[selection - 1]["function"]) # do the function depending on the option
                mainMenu = False
            except IndexError:
                print("\nThat Number is Not Selectable\n")
        except ValueError:
            print("You have to input a number")

openMainMenu()
