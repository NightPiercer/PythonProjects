# Requirments
#     Convert length (standard and metric)
#     Convert volume (standard and metric)
#     Convert temperature (Celsius and Farenheit)

# Scope Creep
#       Cool if the program had a GUI

# Refactoring
#       Make improvements to the code
#       How to make the code more efficient
#       DRY --> Don't Repeat Yourself

# Pseudo Code --> In our own words --> figuring out the logic of the program ---> Comments

# user input as to which conversion they want to do.

while True:
    # Ask user
    userChoice = input('Please select: \n'
                        '\t1.Inches to MM \n'
                        '\t2.MM to Inches \n'
                        '\tQ to Quit\n')
                        # If the user types quit --> Do the same thing as Q

    userChoice = userChoice.upper() # Change a user 'q' to 'Q'
    
    print(userChoice)
    # Create a conditional statement
    if userChoice == '1':
        #conversion from in to mm
        # Convert inches into mm 
        # get the information from the user
        userInches = input('What are the inches? ') # this returns type str

        # Perform the conversion
        # 1 in = 25.4 mm
        outputMM = float(userInches) * 25.4

        # Output the results to the user.
        # EX 1 in   --> The length of 1in. is equal to 25.4mm
        print('The length of ' + userInches + 'in. is equal to ' + str(outputMM) + 'mm')

    elif userChoice == '2':
        #conversion from mm to in
        # Convert mm to inches
        # Get the information from the user
        userMM = input('What are the mm?') # this returns type str

        # Perform the conversion
        # 1 mm = 0.0394 in
        outputInches = float(userMM) / 25.4

        # Output the results to the user.
        # Ex 1 mm    --> The length of 1mm is equal to 0.0394in
        print('The length of ' + userMM + 'mm is equal to ' +str(outputInches) + 'in.')
    elif userChoice[0] == 'Q': #
        break
    else:
        #This is anything that is not 1 or 2.
        print('That is not an option')




