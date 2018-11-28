# conditional statement is used to evaluate a condition.

# if statement ----- if <condition> then <do this>

# if <expr>:
#   <statement>
#   <statement>
# This is not in the if statement

# if <expr> {<statement>}   Used by other languages
# magicNumber = 7
# userNumber = input('Please choose a number (0-9) ')
# print('Your number is ' + str(userNumber) "\n")
# the value entered by the user return as a str
# get the str cast it to an integer

# typeofMagicNumber = type(magicNumber)  # of value type you can't print type
# typeofUserNumber = type(userNumber) # you can only print string

# print("magicNumber " + str(typeofMagicNumber))
# print("userNumber " + str(typeofUserNumber))

# conditional statement to compare the user number with the magic number
# if userNumber == magicNumber: # not just the comparing value also datatype
    # print("\tYou guessed right!")
    # print("\tYou are good at this")
# else:
    # print("\tYou chose poorly")
    # print('\tThe number was' + str(magicNumber))

# print("End of program")

# namePerson = "Alex"
# if namePerson != "Alex": # Name of person is NOT Alex
#     print ('The person is not Alex')
# else: # The person's name is Alex
#     print('The person name is Alex')


# # More evaluations that can be made

# myNumber = 34
# if myNumber < 50:
#     print("Less than 50")

# if myNumber > 50:
#     print ("Greater than 50")

# if myNumber >= 34:
#     print('Greater than or equal to 34')

# if myNumber <= 34:
#     print ('Less than or equal to 34')

# Mulitcondition evaluation

# carKeysOnPerson = True
# batterLevel = 10

# #conditional statement to determine if car starts
# if carKeysOnPerson and batterLevel > 11: # ---AND Both conditions must be met
#     print("start the car")
# else:
#     print("car won't start")

# if carKeysOnPerson or batterLevel > 11: # ---OR Only one condition must be met
#     print("start the car")
# else:
#     print("car won't start")