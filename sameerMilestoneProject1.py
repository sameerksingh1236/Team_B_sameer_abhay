from os import system,name    #this is for updating board instead of printing new one again
def chooseMarker():
    while True:
        Player1=input('Player1 choose marker (X or O): ')
        if Player1=='X' or Player1=='x':
            return ('X','O')
        elif Player1=='O' or Player1=='o':
            return ('O','X')
        else:
            pass

def winner(Board,Player1,Player2):
    if Board[1]==Board[2]==Board[3]!=' ':
        marker=Board[1]
    elif Board[4]==Board[5]==Board[6]!=' ':
        marker=Board[4]
    elif Board[7]==Board[8]==Board[9]!=' ':
        marker=Board[7]    
    elif Board[1]==Board[4]==Board[7]!=' ':
        marker=Board[1]
    elif Board[2]==Board[5]==Board[8]!=' ':
        marker=Board[2]
    elif Board[3]==Board[6]==Board[9]!=' ':
        marker=Board[3]
    elif Board[1]==Board[5]==Board[9]!=' ':
        marker=Board[1]
    elif Board[3]==Board[5]==Board[7]!=' ':
        marker=Board[3]
    else:
        return False
    if marker==Player1:
        return 'Player1'
    else:
        return 'Player2'

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

def DisplayBoard(Board):
    print("{}|{}|{}".format(Board[7],Board[8],Board[9]))
    print("-----")
    print("{}|{}|{}".format(Board[4],Board[5],Board[6]))
    print("-----")
    print("{}|{}|{}".format(Board[1],Board[2],Board[3]))

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
        Board=['NA',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        Player1,Player2 = chooseMarker()
        currentPlayer='Player1'
        chances=0
        while winner(Board,Player1,Player2) is False and chances<9:
            ClearScreen()
            DisplayBoard(Board)
            nextMove(Board,currentPlayer,Player1,Player2)
            chances=chances+1
            if currentPlayer=='Player1':
                currentPlayer='Player2'
            else:
                currentPlayer='Player1'
        if winner(Board,Player1,Player2) is False:
            print('Draw')
        else:        
            print('Winner is '+winner(Board,Player1,Player2))
        newGame=playNewGame()
