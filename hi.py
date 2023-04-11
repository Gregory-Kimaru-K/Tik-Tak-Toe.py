import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

currentPlayer = "X"
winner = None
gamerunning = True

#pinting the game board
def printboard(board):
    print(' '+ board[0] + ' | ' + board[1] + ' ' + '|' + ' ' + board[2])
    
    print('-----------')
    
    print(' '+ board[3] + ' | ' + board[4] + ' ' + '|' + ' ' + board[5])
    
    print('-----------')
    
    print(' '+ board[6] + ' | ' +  board[7] + ' ' + '|' + ' ' + board[8])

#take player input
def playerinput(board):

    imp = int(input("Enter a number (1-9): "))
    if imp >=1 and imp <= 9 and board[imp-1] == "-":
        board[imp-1] = currentPlayer 
    else:
        print("OOPS player is already in this position")


#check for win or tie
def horizontalWinCheck(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[6] != "-":
        winner = board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    
def checkTie(board):
    global gamerunning
    if "-" not in board:
        printboard(board)
        print("Its a tie")
        gamerunning = False

def checkWin():
    global gamerunning
    if checkDiagonal(board) or checkRow(board) or horizontalWinCheck(board):
        printboard(board)
        print(f"The winner is {winner}")
        

        gamerunning = False


#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#quit orcontinue with game
def continuePlaying():
    choice = "Wrong"
    while choice not in ['Y', 'N']:
        choice = input("Please pick the option of (Y or N): ")
        
        if choice not in ['Y','N']:
            print("sorry, I dont understand. Plese pick Y or N ")
            
        if choice== 'Y':
            return True
        else:
            return False

#computer
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

#check for win or tie again
while gamerunning:
        printboard(board)
        playerinput(board)
        checkWin()
        checkTie(board)
        switchPlayer()
        computer(board)
        checkWin()
        checkTie(board)