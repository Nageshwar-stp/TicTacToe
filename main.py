# TicTaCToe
# code by Nageshwar_Tripathi
# dated_4th April 2021

import random
from time import sleep

try:
    from playsound import playsound
    from threading import Thread
except:
    pass

try:
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
except:
    pass

try:
    from termcolor import colored
except:
    pass

gameBoard = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-'],
]

inputSets = ['Q', 'W', 'E', 'A', 'S', 'D', 'Z', 'X', 'C']

level = "smart"

winnerFound = False
winner = None

cpuThinkPhrases = ['epic', 'smart', 'you fool', 'no benefit', 'let\'s see']

def play_music():
    try:
        playsound('background.mp3')
    except:
        pass

try:
    music_thread = Thread(target=play_music)
    music_thread.start()
except:
    pass

def printgameboard():
    print()
    for row in gameBoard:
        for data in row:
            print(colored(data, 'cyan'), end=" ")
            #print(data, end = " ")
        print()

def resistMessage(player):
    try:
        print(colored(f"-----------{player}'s one move resisted!-----------", 'red'))
    except:
        print(f"-----------{player}'s one move resisted!-----------")


def placeInput(position, player):

    marker = None

    if player == 'user':
        marker = 'X'
    elif player == 'cpu':
        marker = 'O'

    if position == 'Q':
        if gameBoard[0][0] == '-':
            gameBoard[0][0] = marker
        else:
            resistMessage(player)

    elif position == 'W':
        if gameBoard[0][1] == '-':
            gameBoard[0][1] = marker
        else:
            resistMessage(player)

    elif position == 'E':
        if gameBoard[0][2] == '-':
            gameBoard[0][2] = marker
        else:
            resistMessage(player)

    elif position == 'A':
        if gameBoard[1][0] == '-':
            gameBoard[1][0] = marker
        else:
            resistMessage(player)

    elif position == 'S':
        if gameBoard[1][1] == '-':
            gameBoard[1][1] = marker
        else:
            resistMessage(player)

    elif position == 'D':
        if gameBoard[1][2] == '-':
            gameBoard[1][2] = marker
        else:
            resistMessage(player)

    elif position == 'Z':
        if gameBoard[2][0] == '-':
            gameBoard[2][0] = marker
        else:
            resistMessage(player)

    elif position == 'X':
        if gameBoard[2][1] == '-':
            gameBoard[2][1] = marker
        else:
            resistMessage(player)

    elif position == 'C':
        if gameBoard[2][2] == '-':
            gameBoard[2][2] = marker
        else:
            resistMessage(player)

    findWinner()

def findWinner():

    players = ['X', 'O']
    global winner

    for play in players:
        if gameBoard[0][0] == play and gameBoard[1][0] == play and gameBoard[2][0] == play:
            winner = play
            break
        elif gameBoard[0][1] == play and gameBoard[1][1] == play and gameBoard[2][1] == play:
            winner = play
            break
        elif gameBoard[0][2] == play and gameBoard[1][2] == play and gameBoard[2][2] == play:
            winner = play
            break

        #--------------------------------------------------------

        elif gameBoard[0][0] == play and gameBoard[0][1] == play and gameBoard[0][2] == play:
            winner = play
            break
        elif gameBoard[1][0] == play and gameBoard[1][1] == play and gameBoard[1][2] == play:
            winner = play
            break
        elif gameBoard[2][0] == play and gameBoard[2][1] == play and gameBoard[2][2] == play:
            winner = play
            break

        #--------------------------------------------------------
        elif gameBoard[0][0] == play and gameBoard[1][1] == play and gameBoard[2][2] == play:
            winner = play
            break
        elif gameBoard[0][2] == play and gameBoard[1][1] == play and gameBoard[2][0] == play:
            winner = play
            break

    if winner != None:
        global winnerFound
        winnerFound = True
        startGame()


def cpuSmartInputs():

    vs = 'X'
    own = 'O'

    try:
        fire = random.choice(inputSets)
    except:
        fire = ""
        print("DRAW")

    # rollings---------------
    t1 = gameBoard[0][0]
    t2 = gameBoard[0][1]
    t3 = gameBoard[0][2]

    m1 = gameBoard[1][0]
    m2 = gameBoard[1][1]
    m3 = gameBoard[1][2]

    b1 = gameBoard[2][0]
    b2 = gameBoard[2][1]
    b3 = gameBoard[2][2]

     # resisting------------------
    if t1 == '-' and ((t2 == vs and t3 == vs) or (m1 == vs and b1 == vs) or (m2 == vs and b3 == vs)):
        fire = 'Q'
    if t2 == '-' and ((t1 == vs and t3 == vs) or (m2 == vs and b2 == vs)):
        fire = 'W'
    if t3 == '-' and ((t1 == vs and t2 == vs) or (m2 == vs and b1 == vs) or (m3 == vs and b3 == vs)):
        fire = 'E'

    if m1 == '-' and ((t1 == vs and b1 == vs) or (m2 == vs and m3 == vs)):
        fire = 'A'
    if m2 == '-' and ((t1 == vs and b3 == vs) or (t3 == vs and b1 == vs) or (t2 == vs and b2 == vs) or (m1 == vs and m3 == vs)):
        fire = 'S'
    if m3 == '-' and ((m1 == vs and m2 == vs) or (t3 == vs and b3 == vs)):
        fire = 'D'

    if b1 == '-' and ((t1 == vs and m1 == vs) or (m2 == vs and t3 == vs) or (b2 == vs and b3 == vs)):
        fire = 'Z'
    if b2 == '-' and ((b1 == vs and b3 == vs) or (m2 == vs and t2 == vs)):
        fire = 'X'
    if b3 == '-' and ((b1 == vs and b2 == vs) or (m2 == vs and t1 == vs) or (m3 == vs and t3 == vs)):
        fire = 'C'

    # defending --------------

    if t1 == '-' and ((t2 == own and t3 == own) or (m1 == own and b1 == own) or (m2 == own and b3 == own)):
        fire = 'Q'
    if t2 == '-' and ((t1 == own and t3 == own) or (m2 == own and b2 == own)):
        fire = 'W'
    if t3 == '-' and ((t1 == own and t2 == own) or (m2 == own and b1 == own) or (m3 == own and b3 == own)):
        fire = 'E'

    if m1 == '-' and ((t1 == own and b1 == own) or (m2 == own and m3 == own)):
        fire = 'A'
    if m2 == '-' and ((t1 == own and b3 == own) or (t3 == own and b1 == own) or (t2 == own and b2 == own) or (m1 == own and m3 == own)):
        fire = 'S'
    if m3 == '-' and ((m1 == own and m2 == own) or (t3 == own and b3 == own)):
        fire = 'D'

    if b1 == '-' and ((t1 == own and m1 == own) or (m2 == own and t3 == own) or (b2 == own and b3 == own)):
        fire = 'Z'
    if b2 == '-' and ((b1 == own and b3 == own) or (m2 == own and t2 == own)):
        fire = 'X'
    if b3 == '-' and ((b1 == own and b2 == own) or (m2 == own and t1 == own) or (m3 == own and t3 == own)):
        fire = 'C'


    inputSets.remove(fire)
    placeInput(fire, 'cpu')
    printgameboard()


def cpuHardInputs():

    vs = 'X'
    own = 'O'

    try:
        fire = random.choice(inputSets)
    except:
        fire = ""
        print("DRAW")

    # rollings---------------
    t1 = gameBoard[0][0]
    t2 = gameBoard[0][1]
    t3 = gameBoard[0][2]

    m1 = gameBoard[1][0]
    m2 = gameBoard[1][1]
    m3 = gameBoard[1][2]

    b1 = gameBoard[2][0]
    b2 = gameBoard[2][1]
    b3 = gameBoard[2][2]


 # resisting------------------
    if t1 == '-' and ((t2 == vs and t3 == vs) or (m1 == vs and b1 == vs) or (m2 == vs and b3 == vs)):
        fire = 'Q'
    if t2 == '-' and ((t1 == vs and t3 == vs) or (m2 == vs and b2 == vs)):
        fire = 'W'
    if t3 == '-' and ((t1 == vs and t2 == vs) or (m2 == vs and b1 == vs) or (m3 == vs and b3 == vs)):
        fire = 'E'

    if m1 == '-' and ((t1 == vs and b1 == vs) or (m2 == vs and m3 == vs)):
        fire = 'A'
    if m2 == '-' and ((t1 == vs and b3 == vs) or (t3 == vs and b1 == vs) or (t2 == vs and b2 == vs) or (m1 == vs and m3 == vs)):
        fire = 'S'
    if m3 == '-' and ((m1 == vs and m2 == vs) or (t3 == vs and b3 == vs)):
        fire = 'D'

    if b1 == '-' and ((t1 == vs and m1 == vs) or (m2 == vs and t3 == vs) or (b2 == vs and b3 == vs)):
        fire = 'Z'
    if b2 == '-' and ((b1 == vs and b3 == vs) or (m2 == vs and t2 == vs)):
        fire = 'X'
    if b3 == '-' and ((b1 == vs and b2 == vs) or (m2 == vs and t1 == vs) or (m3 == vs and t3 == vs)):
        fire = 'C'

    inputSets.remove(fire)
    placeInput(fire, 'cpu')
    printgameboard()


def cpuLowInputs():

    vs = 'X'
    own = 'O'

    try:
        fire = random.choice(inputSets)
    except:
        fire = ""
        print("DRAW")

    inputSets.remove(fire)
    placeInput(fire, 'cpu')
    printgameboard()


def takeInput():

    try:
        engine.say(random.choice(cpuThinkPhrases))
        engine.runAndWait()
    except:
        pass
    print("\n----------- CPU is thinking :")

    sleep(1)

    global level
    if level == 'smart':
        cpuSmartInputs()
    elif level == 'hard':
        cpuHardInputs()
    elif level == 'low':
        cpuLowInputs()

    if len(inputSets) != 0:
        nextInput = str(input("\n----------- Your Input : ")).upper()
        placeInput(nextInput, 'user')

        try:
            inputSets.remove(nextInput)
        except:
            pass
        printgameboard()


def checkProceedings():
    proceedings = 0

    for row in gameBoard:
        for data in row:
            if data == '-':
                proceedings += 1

    return proceedings


def startGame():

    printgameboard()

    while winnerFound == False:
        proceedings = checkProceedings()
        if(proceedings > 0):
            takeInput()
        else:
            break
    if winnerFound == True:

        winnerName = "None"
        if winner == 'X':
            winnerName = "You"
        elif winner == 'O':
            winnerName = 'CPU'

        try:
            print(colored(f"\n-----------{winnerName}, Won the Match!!!-----------", 'magenta'))
            if winnerName == 'CPU':
                engine.say("I, won the match, you looser")
                engine.runAndWait()
            else:
                engine.say("I will see you next time")
                engine.runAndWait()
        except:
            print(f"\n-----------{winnerName}, Won the Match!!!-----------")

        remainingSlots = len(inputSets)

        if(winnerName == "You"):
            appreciation = ""
            if remainingSlots == 4:
                appreciation = "LEGENDARY"
            elif remainingSlots == 3:
                appreciation = "EPIC"
            elif remainingSlots == 2:
                appreciation = "SMART"
            elif remainingSlots == 1:
                appreciation = "COMPETITIVE"
            elif remainingSlots == 0:
                appreciation = "DO OR DIE"
            else:
                appreciation = "IMPOSSIBLE"

            try:
                print(colored(f"-----------{appreciation} Winning!-----------\n", 'blue'))
                engine.say(f"{appreciation} Winning")
                engine.runAndWait()
            except:
                print(f"-----------{appreciation} Winning!-----------\n")

        elif (winnerName == "CPU"):
            appreciation = ""
            if remainingSlots == 4:
                appreciation = "DIRTY"
            elif remainingSlots == 3:
                appreciation = "CONSPIRACIAL"
            elif remainingSlots == 2:
                appreciation = "NOT BEARABLE"
            elif remainingSlots == 1:
                appreciation = "COMPETITIVE"
            elif remainingSlots == 0:
                appreciation = "DIE HARD"
            else:
                appreciation = "IMPOSSIBLE"

            try:
                print(colored(f"-----------{appreciation} LOSING!-----------\n", 'red'))
                engine.say(f"{appreciation} Losing")
                engine.runAndWait()
            except:
                print(f"-----------{appreciation} LOSING!-----------\n")


        exit()

    if winnerFound == False and len(inputSets) <= 0:
        try:
            print(colored("\n----------- MATCH DRAW -----------\n", 'yellow'))
            engine.say("Ohhhsh! MATCH DRAW")
            engine.runAndWait()
        except:
            print("\n----------- MATCH DRAW -----------\n")
        exit()


sleep(1)
print("\nSTP'S TIC TAC TOE\n")
sleep(1)
print("""Key mappings

Q W E
A S D
Z X C
---------------        """)
sleep(2)

levelInput = str(input("\n LEVEL (Smart/Hard/Low) : (s/h/l) : ")).lower()
if levelInput == 's':
    level = "smart"
elif levelInput == 'h':
    level = 'hard'
elif levelInput == 'l':
    level = 'low'
else:
    print("Not Valid! (Defaulting to Smart)")
sleep(1)
print()
startGame()
