import random
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).
# The dice sum will be the output of this function.


def randDice():
# Write your logic to generate 2 numbers between 1 and 6 here
    rollTheDice = random.randint(1,6)
    rollTheDice2 = random.randint(1, 6)

    total = rollTheDice + rollTheDice2 #Getting the sum of the two dice that were rolled.
    return total
   # Sum 2 numbers
   # return sum to calling function

# Then write a mainline that calls the "randDice" function 100 times in a for loop.
totalRolls = 0
numberOfRolls = 100

for count in range(1,numberOfRolls):
    currentRoll = randDice()
    totalRolls += currentRoll #Accumulate the total.

# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
averageRoll = round(totalRolls / numberOfRolls,2) #Get the average of the 100 rolls.
print('the average of the 100 rolls is:', averageRoll)#Print the average of the 100 rolls.
