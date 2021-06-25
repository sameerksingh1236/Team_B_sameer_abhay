from os import system,name

from numpy.core.fromnumeric import diagonal    #this is for updating board instead of printing new one again
def chooseMarker():
    while True:
        Player1=input('Player1 choose marker (X or O): ')
        if Player1=='X' or Player1=='x':
            return ('X','O')
        elif Player1=='O' or Player1=='o':
            return ('O','X')
        else:
            pass

def winner(Board,Player1,sizeBoard):     #removed Player2 from this function as it was not needed
    #implementing for generalized nXn dimension board

    for row in range(sizeBoard):       #Rows check
        currentRow=Board[row][0]
        if currentRow == ' ':
            continue
        for col in range(sizeBoard):
            if Board[row][col]!=currentRow:
                break
            if col==sizeBoard-1 and currentRow==Player1:
                return 'Player1'
            else:
                return 'Player2'

    for col in range(sizeBoard):       #Columns check
        currentCol=Board[0][col]
        if currentCol == ' ':
            continue
        for row in range(sizeBoard):
            if Board[row][col]!=currentCol:
                break
            if row==sizeBoard-1 and currentCol==Player1:
                return 'Player1'
            else:
                return 'Player2'
    
    diagonal1=Board[0][0]              #First Diagonal elements check
    if diagonal1!=' ':
        for row in range(sizeBoard):
            if diagonal1!=Board[row][row]:
                break
            if row==sizeBoard-1 and diagonal1==Player1:
                return 'Player1'
            else:
                return 'Player2'

    diagonal2=Board[0][sizeBoard-1]    #Second Diagonal elements check
    if diagonal2!=' ':
        for row in range(sizeBoard):
            if diagonal2!=Board[row][sizeBoard-row-1]:
                break
            if row==sizeBoard-1 and diagonal2==Player1:
                return 'Player1'
            else:
                return 'Player2'

    return False     


def nextMove(Board,currentPlayer,Player1,Player2):
    position='0'
    while position.isdigit() is False or int(position)>9 or int(position)<1 or Board[int(position)]!=' ':
        if currentPlayer=='Player1':
            marker=Player1
        else:
            marker=Player2
        position=input('Enter an empty position from 1-9 for {} ({}):'.format(currentPlayer,marker))
    position=int(position)
    if currentPlayer=='Player1':
        Board[position]=Player1
    else:
        Board[position]=Player2

def ClearScreen():
    if name=='nt':
        _=system('cls')
    else:
        _=system('clear')

def DisplayBoard(Board,sizeBoard=3):
    #print("{}|{}|{}".format(Board[7],Board[8],Board[9]))
    #print("-----")
    #print("{}|{}|{}".format(Board[4],Board[5],Board[6]))
    #print("-----")
    #print("{}|{}|{}".format(Board[1],Board[2],Board[3]))

# The above code has been generalized for n-dimension Board.
    for i in range(2*sizeBoard-1):
        for j in range(2*sizeBoard-1):
            if i%2==0:
                if j%2==0:
                    print(Board[i//2][j//2],end='')
                else:
                    print('|',end='')
            else:
                print('-',end='')
        print()

def playNewGame():
    while True:
        newgame=input('Want to play another game?(Y/N) :')
        if newgame=='Y' or newgame=='y':
            return True
        if newgame=='N' or newgame=='n':
            return False
        else:
            pass

if __name__=='__main__':
    newGame=True
    while newGame is True:
        sizeBoard=3  #A boardSize() func can be implemented to input valid board sizes
        Board=[[' ' for __ in range(sizeBoard)] for _ in range(sizeBoard)]
        #Board=['NA',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        Player1,Player2 = chooseMarker()
        currentPlayer='Player1'
        chances=0
        while winner(Board,Player1) is False and chances<sizeBoard**2:
            ClearScreen()
            DisplayBoard(Board)
            nextMove(Board,currentPlayer,Player1,Player2)
            chances=chances+1
            if currentPlayer=='Player1':
                currentPlayer='Player2'
            else:
                currentPlayer='Player1'
        if winner(Board,Player1) is False:
            print('Draw')
        else:        
            print('Winner is '+winner(Board,Player1))
        newGame=playNewGame()
