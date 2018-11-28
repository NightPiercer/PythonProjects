# Loop --> continues to execute the statement within until a condition is met

# for loop
# for loop sytax
#   for <item in a list> in <the list>
#       <statement>
#       exit out of the loop when reach end of the list
# count = 0

# favoriteGames = ['Skyrim', 'Mass Effect', 'Red Dead 2', 'Shadow of War']
# for game in favoriteGames: # Game is 4 elements long #execute until the end of the list
#     print(game)
#     count += 1
#     print (count)

# sumOfNumbers = 0
# listOfNumbers = [1,2,3,4,5,6,7,8,9]
# for number in listOfNumbers:
#     print(number)
#     sumOfNumbers += number  # sumOfNumber = sumOfNumber + number
#     print ("The current sum is " + str(sumOfNumbers))

# for number in range(1,20,2):
#     print (number)

# # end the loop early
# for number in range(1,20):
#     if number > 5:
#         break
#     print (number)

# skip a statement in the loop
# for number in range(1,20):
#     if number == 5:
#         continue
#     print (number)

# While Loops -- Executing the code in the loop WHILE a condition exists
# Typically use while when you have a unknown condition

# outsideTemp = 80 # can't have a fixed value this would need to change over time
# while outsideTemp < 90:
#     print("It's cold")
