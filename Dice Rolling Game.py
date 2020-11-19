
import random
def diceNum(): #This function is what assigns a number to the dice
    dice = random.randint(1,6) #The random.randint(1,6) will assign dice a number between 1,6
    print('You have rolled:',dice)

def diceRoll(): #This function is the actual game.
    counter = 0 #This count how many times the user rolls the dice
    while True: #Condtional for loop
        choice = input("Press enter to roll the dice, type 'end' to end game: ")
        if choice == '': #When the user presses enter, the dice will be rolled,
                         #the diceNum() will be called and the counter will be increased by 1
            diceNum()
            counter += 1
            c2 = input("Would You Like to roll again? Yes/No: ")
            if c2 == 'Yes': #The game will restart with a different
                            #outcome everytime.
                continue
            elif c2 == 'No': #The game will end and the amount of times the user rolled
                             #will be printed to the user.
                print('Have a good day, user!')
                print('You have rolled:',counter,'times')
                break
            else:
                print("That's not a valid input.") #This is a fallsafe incase the user types
                                                    #the wrong input.
        elif choice == 'end': #Game will end, then it prints how many times the user rolled.
            print('Have a good day user!')
            print('You have rolled:',counter,'times')
            break
        
diceRoll()
#I used two functions to avoid repeating code over and over for each condtion.
#Functions will allow the program to be easier to read.
            
