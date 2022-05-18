#connect four
board = [['-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-']]



def display_board():
    print('  1   2   3   4   5   6   7')
    print('| ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + ' | ' + board[0][3] + ' | ' + board[0][4] + ' | ' + board[0][5] + ' | ' + board[0][6] + ' |')
    print('| ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + ' | ' + board[1][3] + ' | ' + board[1][4] + ' | ' + board[1][5] + ' | ' + board[1][6] + ' |')
    print('| ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2] + ' | ' + board[2][3] + ' | ' + board[2][4] + ' | ' + board[2][5] + ' | ' + board[2][6] + ' |')
    print('| ' + board[3][0] + ' | ' + board[3][1] + ' | ' + board[3][2] + ' | ' + board[3][3] + ' | ' + board[3][4] + ' | ' + board[3][5] + ' | ' + board[3][6] + ' |')
    print('| ' + board[4][0] + ' | ' + board[4][1] + ' | ' + board[4][2] + ' | ' + board[4][3] + ' | ' + board[4][4] + ' | ' + board[4][5] + ' | ' + board[4][6] + ' |')
    print('| ' + board[5][0] + ' | ' + board[5][1] + ' | ' + board[5][2] + ' | ' + board[5][3] + ' | ' + board[5][4] + ' | ' + board[5][5] + ' | ' + board[5][6] + ' |')


def player1():
    while True:
        while True:
            while True:
                column = input('Which column would you like to place your piece (O) in (1 to 7)? ')
                try:
                    column = int(column)
                except:
                    print('Please enter a Number.') 

                if type(column) == int:
                    break                   
                
            column = column - 1
                
                
            if column <= 6 and column >= 0:
                break
            else:
                print('Invalid Column.')
        i = 5
        while i >= 0:
            if board[i][column] != '-':
                if i > -1:
                    i -= 1
            else:
                board[i][column] = 'O'
                break
        if (board[i][column] == 'O' or board[i][column] == 'X') and i == -1:
            display_board()
            print('Column is Full!')
        else:
            break
        

def player2():
    while True:
        while True:
            while True:
                column = input('Which column would you like to place your piece (X) in (1 to 7)? ')
                try:
                    column = int(column)
                except:
                    print('Please enter a Number.')
                if type(column) == int:
                    break
                
            column = column - 1

            if column <= 6 and column >= 0:
                break
            else:
                print('Invalid Column.')
        i = 5
        while i >= 0:
            if board[i][column] != '-':
                if i > -1:
                    i -= 1
            else:
                board[i][column] = 'X'
                break
        if (board[i][column] == 'O' or board[i][column] == 'X') and i == -1:
            display_board()
            print('Column is Full!')
        else:
            break

def checkwin_horizontal():
    i = 5
    while i >= 0:
        for col in range(len(board)-2):
            if board[i][col] == 'O' and board[i][col+1] == 'O' and board[i][col+2] == 'O' and board[i][col+3] == 'O': 
                return 'The Winner is O!'
            if board[i][col] == 'X' and board[i][col+1] == 'X' and board[i][col+2] == 'X' and board[i][col+3] == 'X':
                return 'The Winner is X!'
        
        i = i - 1
        
        if i == -1:
            break

def checkwin_vertical():
    col = 0
    while col <= 6:
        for i in range(len(board)-3):
            if board[i][col] == 'O' and board[i+1][col] == 'O' and board[i+2][col] == 'O' and board[i+3][col] == 'O':
                return 'The Winner is O!'
            if board[i][col] == 'X' and board[i+1][col] == 'X' and board[i+2][col] == 'X' and board[i+3][col] == 'X':
                return 'The Winner is X!'
            
        col += 1
        if col == 7:
            break

def checkwin_diagonal():
    col = 0
    row = 2

    while col <= 3:
        for i in range(len(board)):
            if board[row][col] == 'O' and board[row+1][col+1] == 'O' and board[row+2][col+2] == 'O' and board[row+3][col+3] == 'O':
                return 'The Winner is O!'
            if board[row][col] == 'X' and board[row+1][col+1] == 'X' and board[row+2][col+2] == 'X' and board[row+3][col+3] == 'X':
                return 'The Winner is X!'
        if row >= 0:
            row = row - 1
        else:
            row = 2
            col += 1
    
    col = 6
    row = 2
    while col >= 3:
        for i in range(len(board)):
            if board[row][col] == 'O' and board[row+1][col-1] == 'O' and board[row+2][col-2] == 'O' and board[row+3][col-3] == 'O':
                return 'The Winner is O!'
            if board[row][col] == 'X' and board[row+1][col-1] == 'X' and board[row+2][col-2] == 'X' and board[row+3][col-3] == 'X':
                return 'The Winner is X!'
        if row >= 0:
            row = row - 1
        else:
            row = 2
            col -= 1
        
def check_if_tie():
    list = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            list.append(board[i][j])

    count = list.count('-')
    if count == 0:
        return 'The Game is a Tie!'


def play():
    while True:
        
        display_board()
        print('------------------------------------')
        player1()
        if checkwin_horizontal() == 'The Winner is O!' or checkwin_vertical() == 'The Winner is O!' or checkwin_diagonal() == 'The Winner is O!':
            display_board()
            print('The Winner is O!')
            break
        
        if check_if_tie() == 'The Game is a Tie!':
            print('The Game is a Tie!')
            break
        
        display_board()
        print('------------------------------------')
        player2()
        if checkwin_horizontal() == 'The Winner is X!' or checkwin_vertical() == 'The Winner is X!' or checkwin_diagonal() == 'The Winner is X!':
            display_board()
            print('The Winner is X!')
            break
        if check_if_tie() == 'The Game is a Tie!':
            print('The Game is a Tie!')
            break
        
play()