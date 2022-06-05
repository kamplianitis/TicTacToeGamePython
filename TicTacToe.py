import numpy as np


def printMenu():
    print("Welcome to the tic tac toe game:")
    print("Select one of the options below")
    print("(1) New game")
    print("(2) Quit game")


def endgame(firstplayer, end, gametable=[]):
    if gametable[0][0] == firstplayer and gametable[1][0] == firstplayer and gametable[2][0] == firstplayer:
        end = 1
    elif gametable[0][1] == firstplayer and gametable[1][1] == firstplayer and gametable[2][1] == firstplayer:
        end = 1
    elif gametable[0][2] == firstplayer and gametable[1][2] == firstplayer and gametable[2][2] == firstplayer:
        end = 1
    elif gametable[0][0] == firstplayer and gametable[0][1] == firstplayer and gametable[0][2] == firstplayer:
        end = 1
    elif gametable[1][0] == firstplayer and gametable[1][1] == firstplayer and gametable[1][2] == firstplayer:
        end = 1
    elif gametable[2][0] == firstplayer and gametable[2][1] == firstplayer and gametable[2][2] == firstplayer:
        end = 1
    elif gametable[0][0] == firstplayer and gametable[1][1] == firstplayer and gametable[2][2] == firstplayer:
        end = 1
    elif gametable[0][2] == firstplayer and gametable[1][1] == firstplayer and gametable[2][0] == firstplayer:
        end = 1
    else:
        end = 0
    return end


def gameplay(firstplayer):
    print("We now creating the environment.")
    # create the table
    gametable = np.zeros([3, 3])
    print(gametable)
    end = 0
    count = 9

    while end == 0 and count != 0:
        print("Player ", firstplayer, "is now playing.")
        choicex, choicey = input("Give your choice here").split()
        try:
            choicex = int(choicex)
            choicey = int(choicey)
        except:
            print("not correct values")
        # now i have to check if the values are in range or there is already a value there
        if 1 <= choicex <= 3 and 1 <= choicey <= 3:
            if gametable[choicex - 1][choicey - 1] == 0:
                gametable[choicex - 1][choicey - 1] = firstplayer
                end = endgame(firstplayer, end, gametable)
                if end == 0:
                    count = count - 1
                # change the player so that we can move on the next player
                if firstplayer == 1 and (end == 0 and count != 0):
                    firstplayer = 2
                elif firstplayer == 2 and (end == 0 and count != 0):
                    firstplayer = 1
            else:
                print("Move has already been done there. Please try again \n")
        else:
            print("Values are out of range")
        print(gametable)
    if end == 1:
        print("Game over: Player", firstplayer, "has won!!!")
    else:
        print("The game ended as a draw")


def selectplayer():
    while (1):
        firstplayer = input("Give the player who is going to play first: ")
        try:
            firstplayer = int(firstplayer)
            if firstplayer == 1 or firstplayer == 2:
                print("The first player to play will be", firstplayer, "\n")
                return firstplayer
            else:
                print("ERROR:Give a value between 1 and 2")
        except:
            print("ERROR:Give an integer between 1 and 2")


# first thing we need to do is print the menu as long as we don't get a choice
while 1:
    printMenu()
    menuoption = input("Give your choice: ")
    try:
        menuoption = int(menuoption)
        if menuoption == 1:
            firstplayer = selectplayer()
            gameplay(firstplayer)
        elif menuoption == 2:
            print("Thank you for playing. Goodbye!!")
            break
        else:
            print("Give a value between 1 and 2 \n")
    except:
        print("Give a value that is allowed \n")
