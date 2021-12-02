#this is a game that has the following requirements
#There should be a board
#Let's build our first part of the code
board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

#this will let us know whether the game is over or not yet
game_still_on = True

#this bit will tell us the winner
winner = None

#this bit will tell us the current player
current_player = "X"

#------this chunk of the code will outline the functions
def play_game():
    display_board()  #this will display the game board

    #let's introduce a loop until a winner is acquired
    while game_still_on:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

#checks for who the winner is going to be
        if winner == "X" or winner == "O":
            print(winner +"Won")
        elif winner == None:
            print("tie!")

#Display the game board on screen
def display_board():
    print("\n")
    print(board[0] + "|" + board[1] + "|" + board[2] + " 1|2|3")
    print(board[3] + "|" + board[4] + "|" + board[5] + " 4|5|6")
    print(board[6] + "|" + board[7] + "|" + board[8] + " 7|8|9")
    print("\n")


#this part will handle the turn-taking for the players
def handle_turn(player):

    #get the position of the player
    print(player + "'s turn")
    position = input("Choose a position from 1-9: ")

    #whatever the user inputs, make sure it's valid
    valid = False
    while not valid:
        while position not in["1", "2", "3", "4", "5", "6", "7", "8", "9"]: 
            position = input("choose a position from 1-9: ")

            position = int(position)-1

            if board[position] == "-":
                valid = True
            else:
                 print("You can't go there. Try again")

            #put the game piece in the board
            board[position] = player

            #display the game board
            display_board()


#check whether the game is over
def check_if_game_over():
    check_for_winner()
    check_for_tie()

#check if somebody has won 
def check_for_winner():
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()


#get the winners in the game
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

#check the winning sections 
#row winner
def check_rows():
    global game_still_on

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    #if any row does have a match, declare a win
    if row_1 or row_2 or row_3:
        game_still_on = False

#return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None


#column winner
def check_columns():
    global game_still_on

    column_1 = board[0] == board[3] == board[6] !="-"
    column_2 = board[1] == board[4] == board[7] !="-"
    column_3 = board[2] == board[5] == board[8] !="-"

    if column_1 or column_2 or column_3:
        game_still_on = False

    #return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None

#diagonal winner
def check_diagonals():
    global game_still_on

    diagonal_1 = board[0] == board[4] == board[8] !="-"
    diagonal_2 = board[2] == board[4] == board[6] !="-"

    if diagonal_1 or diagonal_2:
        game_still_on = False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None


#the next piece of this puzzle is to check for a tie
def check_for_tie():
    global game_still_on

    if "-" not in board:
        game_still_on = False
        return True
    else:
        return False


#This snippet describes how the plays will be flipped
def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"

#Our Tic Tac Toe game is now complete
#Now let's execute the game
play_game()




