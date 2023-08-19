#VARIABLES---------------------------------------------------------------------
i = 1

#FUNCTIONS---------------------------------------------------------------------
def playGame():
    global i
    startGame = input("Type 'PLAY' To Start The Game: ")
    startGame = startGame.lower()

    if startGame == "play": 
        from random import choice #imports choice function from random module
        userName = input("\nEnter Your Name: ") #takes the user input.e.g what username to register
        data = open(userName+".txt","w+")
        data.close()
        print ("\nRULES: Rock breaks Scissors, Scissors cuts Paper, Paper covers Rock.\nScore 5 Points to win.\nType 'Quit' to end the session.")
        rps = ['r','p','s']
        userScore = 0
        cpuScore = 0

        while True:
            print ("Score -> " + str(userName) + ": " + str(userScore) + "  CPU: " + str(cpuScore))
            print ("\nR: Rock      P: Paper     S: Scissor\n")
            print ("------------------------------------------------")
            userInput = input("Enter Your Choice: ")   
            userInput = userInput.lower()
            cpuInput = choice(rps)#Look into this as well.

            if userInput == cpuInput: #If the round ends in a tie.
                if(userInput == 'r'):
                    print("We both chose ROCK.")
                if(userInput == 'p'):
                    print("We both chose PAPER.")
                if(userInput == 's'):
                    print("We both chose SCISSORS.")
                print ("Tie!, Let\'s try again\n")

            elif userInput == 'r' and cpuInput == 's': #Rock > Scissors
                print ('\nYou Win! You entered ROCK. I had SCISSORS.\n')
                userScore+=1
            elif userInput == 'r' and cpuInput == 'p': #Rock < Paper
                print ('\nYou Lose! You entered ROCK. I had PAPER.\n')
                cpuScore+=1
            elif userInput == 's' and cpuInput == 'p': #Scissors > Paper
                print ('\nYou Win! You entered SCISSORS. I had PAPER.\n')
                userScore+=1
            elif userInput == 's' and cpuInput == 'r': #Scissors < Rock
                print ('\nYou Lose! You entered SCISSORS. I had ROCK.\n')
                cpuScore+=1
            elif userInput == 'p' and cpuInput == 's': #Paper < Scissors
                print ('\nYou Lose! You entered PAPER. I had SCISSORS.\n')
                cpuScore+=1
            elif userInput == 'p' and cpuInput == 'r': #Paper > Rock
                print ('\nYou Win! You entered PAPER. I had ROCK.\n')
                userScore+=1

            if cpuScore == 5: #If the CPU wins the game.
                print ("\nScore -> " + str(userName) + ": " + str(userScore) + "  CPU: " + str(cpuScore))
                print ("Better luck next time " + userName + ", You Lose!\n")
                openScore = open("top10.txt","a") 
                openScore.write(str(i) + ": CPU: " + str(cpuScore) + "\n") 
                openScore.close()
                i+=1
                playGame()
                break
            elif userScore == 5: #If the User wins the game.
                print ("\nScore -> " + str(userName) + ": " + str(userScore) + "  CPU: " + str(cpuScore))
                print ("Congratulations " + userName + " you beat me! How about we play again?\n")
                openScore = open("top10.txt","a")
                openScore.write(str(i) + ": " + str(userName) + ": " + str(userScore) + "\n") 
                openScore.close()
                i+=1
                playGame()
                break

            if userInput == "quit":
                break
    elif startGame == "quit":
        return 
    else:
        print ("\nWRONG INPUT! Type In 'PLAY' To Start.\n")
        playGame()

#MAIN EXECUTION---------------------------------------------------------------------
playGame()   