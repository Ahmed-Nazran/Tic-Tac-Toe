player = 1
Win = 1
Draw = -1
Running = 0
Stop = 1
Game = Running
Mark = 'X'
b = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
class color:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YEL = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
def Board():
    print(" {}| {} | {} ".format(b[1],b[2],b[3]))
    print("__|___|__")    
    print(" {}| {} | {} " .format(b[4],b[5],b[6]))
    print("__|___|__")    
    print(" {}| {} | {} ".format(b[7],b[8],b[9]))
    print("  |   |   ")
def CheckPosition(x):
    if(b[x] == ' '):
        return True
    else:
        return False
def CheckWin():
    global Game
    if(b[1] == b[2] and b[2] == b[3] and b[1] != ' '):
        Game = Win
    elif(b[4] == b[5] and b[5] == b[6] and b[4] != ' '):
        Game = Win
    elif(b[7] == b[8] and b[8] == b[9] and b[7] != ' '):
        Game = Win
    elif(b[1] == b[4] and b[4] == b[7] and b[1] != ' '):
        Game = Win
    elif(b[2] == b[5] and b[5] == b[8] and b[2] != ' '):
        Game = Win
    elif(b[3] == b[6] and b[6] == b[9] and b[3] != ' '):
        Game=Win
    elif(b[1] == b[5] and b[5] == b[9] and b[5] != ' '):
        Game = Win
    elif(b[3] == b[5] and b[5] == b[7] and b[5] != ' '):
        Game=Win
    elif(b[1]!=' ' and b[2]!=' ' and b[3]!=' ' and b[4]!=' ' and b[5]!=' ' and b[6]!=' ' and b[7]!=' ' and b[8]!=' ' and b[9]!=' '):    
        Game=Draw
    else:
        Game=Running
print(color.BLUE +"Tic-Tac-Toe Game Created by Nazran"+ color.ENDC)
print(color.CYAN+"Player 1 [X] --- Player 2 [O]\n"+color.ENDC)
while(Game == Running):
    Board()
    if(player % 2 != 0):
        print(color.RED+"Player 1's chance")
        Mark = 'X'
    else:
        print(color.GREEN+"Player 2's chance")
        Mark = 'O'
    choice = int(input("Enter the position between [1-9] where you want to mark : "))
    if(CheckPosition(choice)):
        b[choice] = Mark
        player+=1
        CheckWin()
    else:
        choice = int(input("Please Enter the position between [1-9] where you want to mark : "))
Board()
if(Game==Draw):
    print(color.YEL+"Game Draw"+color.ENDC)
elif(Game==Win):
    player-=1
    if(player%2!=0):
        print(color.YEL+"Player 1 Won"+color.ENDC)
    else:
        print(color.YEL+"Player 2 Won"+color.ENDC)