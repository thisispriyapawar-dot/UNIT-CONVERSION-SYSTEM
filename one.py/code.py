#NAME:Priya Pawar
#ERP:RU-26-02041
#PS NO.:17
#SECTION:B5
#SEMESTER:1ST
#YEAR:1ST
#COURSE:B.TECH 
#BRANCH:Cybersecurity

#----------------------------------------------------------------------------------------------------------------------------------->

# Unit Conversion System - PS 17
# This program converts Length, Weight, Temperature and Time units
# User selects from menu and enters a value to convert

#----------------------------------------------------------------------------------------------------------------------------------->

# Function for Length Conversion
def length_conversion():
    # Showing length conversion options to user
    print("1. km to miles")
    print("2. miles to km")
    print("3. m to cm")
    print("4. cm to m")
    try:
        # Taking sub-choice and value from user
        choice = int(input("Enter your choice: "))
        value = float(input("Enter value: "))
    except ValueError:
        # If user enters non-numeric value
        print("Invalid value. Enter a number.")
        return

    # Checking which length conversion user selected
    if choice == 1:
        # Formula: 1 km = 0.621371 miles
        result = value * 0.621371
        print(f"{value:g} km = {result:.2f} miles")
    elif choice == 2:
        # Formula: miles to km
        result = value / 0.621371
        print(f"{value:g} miles = {result:.2f} km")
    elif choice == 3:
        # Formula: 1 m = 100 cm
        result = value * 100
        print(f"{value:g} m = {result:.2f} cm")
    elif choice == 4:
        # Formula: 1 cm = 0.01 m
        result = value / 100
        print(f"{value:g} cm = {result:.2f} m")
    else:
        # If choice is not 1 to 4
        print("Invalid choice. Select 1 to 4.")

# Function for Weight Conversion
def weight_conversion():
    # Showing weight conversion options to user
    print("1. kg to g")
    print("2. g to kg")
    print("3. kg to pounds")
    print("4. pounds to kg")
    try:
        # Taking sub-choice and value from user
        choice = int(input("Enter your choice: "))
        value = float(input("Enter value: "))
    except ValueError:
        # If user enters non-numeric value
        print("Invalid value. Enter a number.")
        return

    # Checking which weight conversion user selected
    if choice == 1:
        # Formula: 1 kg = 1000 g
        result = value * 1000
        print(f"{result:.2f} g")
    elif choice == 2:
        # Formula: 1 g = 0.001 kg
        result = value / 1000
        print(f"{result:.2f} kg")
    elif choice == 3:
        # Formula: 1 kg = 2.20462 pounds
        result = value * 2.20462
        print(f"{result:.2f} pounds")
    elif choice == 4:
        # Formula: pounds to kg
        result = value / 2.20462
        print(f"{result:.2f} kg")
    else:
        # If choice is not 1 to 4
        print("Invalid choice. Select 1 to 4.")

# Function for Temperature Conversion
def temperature_conversion():
    # Showing temperature conversion options to user
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    try:
        # Taking sub-choice and value from user
        choice = int(input("Enter your choice: "))
        value = float(input("Enter value: "))
    except ValueError:
        # If user enters non-numeric value
        print("Invalid value. Enter a number.")
        return

    # Checking which temperature conversion user selected
    if choice == 1:
        # Formula: F = (C * 9/5) + 32
        result = (value * 9 / 5) + 32
        print(f"{value:g} C = {result:.2f} F")
    elif choice == 2:
        # Formula: C = (F - 32) * 5/9
        result = (value - 32) * 5 / 9
        print(f"{value:g} F = {result:.2f} C")
    else:
        # If choice is not 1 or 2
        print("Invalid choice. Select 1 to 4.")

# Function for Time Conversion
def time_conversion():
    # Showing time conversion options to user
    print("1. hours to minutes")
    print("2. minutes to hours")
    print("3. minutes to seconds")
    print("4. seconds to minutes")
    try:
        # Taking sub-choice and value from user
        choice = int(input("Enter your choice: "))
        value = float(input("Enter value: "))
    except ValueError:
        # If user enters non-numeric value
        print("Invalid value. Enter a number.")
        return

    # Checking which time conversion user selected
    if choice == 1:
        # Formula: 1 hour = 60 minutes
        result = value * 60
        print(f"{result:.2f} minutes")
    elif choice == 2:
        # Formula: 1 minute = 1/60 hour
        result = value / 60
        print(f"{result:.2f} hours")
    elif choice == 3:
        # Formula: 1 minute = 60 seconds
        result = value * 60
        print(f"{result:.2f} seconds")
    elif choice == 4:
        # Formula: 1 second = 1/60 minute
        result = value / 60
        print(f"{result:.2f} minutes")
    else:
        # If choice is not 1 to 4
        print("Invalid choice. Select 1 to 4.")

# Main function - program starts from here
def main():
    # Showing main menu to user
    print("--- Unit Conversion System ---")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Time")
    try:
        # Taking main menu choice from user
        choice = int(input("Enter your choice: "))
    except ValueError:
        # If user enters non-numeric value
        print("Invalid value. Enter a number.")
        return

    # Calling function according to user's choice
    if choice == 1:
        length_conversion()
    elif choice == 2:
        weight_conversion()
    elif choice == 3:
        temperature_conversion()
    elif choice == 4:
        time_conversion()
    else:
        # If choice is not 1 to 4
        print("Invalid choice. Select 1 to 4.")

# Calling main function to run the program
main()