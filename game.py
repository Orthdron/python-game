import random

def check_if_won(board, piece):
    return (
            (board[0] == piece and board[1] == piece and board[2] == piece)
            or
            (board[0] == piece and board[3] == piece and board[6] == piece)
            or
            (board[0] == piece and board[4] == piece and board[8] == piece)
            or
            (board[3] == piece and board[4] == piece and board[5] == piece)
            or
            (board[6] == piece and board[7] == piece and board[8] == piece)
            or
            (board[6] == piece and board[4] == piece and board[2] == piece)
    )


def get_board_number(row, column):
    if row == 1:
        final = 0
    elif row == 2:
        final = 3
    else:
        final = 6
    return final + column - 1


def check_if_vacant(board, row, column):
    if board[get_board_number(row, column)] == '':
        return True
    else:
        return False


def print_board(board):
    for i in range(9):
        z = board[i]
        if board[i] == '':
            z = '_'
        print(' {}'.format(z), end='')
        if i == 2 or i == 5:
            print("\n-------------")
        elif i == 8:
            print("")
        else:
            print(" | ", end='')


def get_message(selection1, selection2):
    combo1 = ['rock', 'paper']
    if selection1 in combo1 and selection2 in combo1:
        return "Paper covers rock"
    combo2 = ['rock', 'scissors']
    if selection1 in combo2 and selection2 in combo2:
        return "Rock crushes Scissors"
    combo3 = ['rock', 'lizard']
    if selection1 in combo3 and selection2 in combo3:
        return "Rock crushes Lizard"
    combo4 = ['rock', 'spock']
    if selection1 in combo4 and selection2 in combo4:
        return "Spock vaporizes rock"
    combo5 = ['scissors', 'paper']
    if selection1 in combo5 and selection2 in combo5:
        return "Scissors cut paper"
    combo6 = ['scissors', 'lizard']
    if selection1 in combo6 and selection2 in combo6:
        return "Scissors decapitates Lizard"
    combo7 = ['scissors', 'spock']
    if selection1 in combo7 and selection2 in combo7:
        return "Spock smashes Scissors"
    combo8 = ['spock', 'lizard']
    if selection1 in combo8 and selection2 in combo8:
        return "Lizard poisons Spock"
    combo9 = ['spock', 'paper']
    if selection1 in combo9 and selection2 in combo9:
        return "Paper disproves Spock"
    combo10 = ['lizard', 'paper']
    if selection1 in combo10 and selection2 in combo10:
        return "Lizard eats Paper"


def selection_winner(userselection, computer_selection):
    message = get_message(userselection, computer_selection)
    rockwinner = ['scissors', 'lizard']
    scissorswinner = ['paper', 'lizard']
    spockwinner = ['rock', 'scissors']
    lizardwinner = ['paper', 'spock']
    paperwinner = ['rock', 'spock']
    if userselection == "rock" and computer_selection in rockwinner:
        win = True
    elif userselection == "scissors" and computer_selection in scissorswinner:
        win = True
    elif userselection == "spock" and computer_selection in spockwinner:
        win = True
    elif userselection == "lizard" and computer_selection in lizardwinner:
        win = True
    elif userselection == "paper" and computer_selection in paperwinner:
        win = True
    else:
        win = False
    return {'win': win, 'message': message}

def playgame():
    print("Let's begin, shall we?")
    player1 = dict(name='', piece='')
    player2 = dict(name='', piece='')
    while player1['name'] == player2['name']:
        player1['name'] = input("Player 1 enter your name: ")
        player2['name'] = input("Player 2 enter your name: ")

    if random.randint(1, 2) == 1:
        player1['piece'] = 'x'
        player2['piece'] = 'o'
        currentPlayer = player1
    else:
        player1['piece'] = 'o'
        player2['piece'] = 'x'
        currentPlayer = player2
    print(currentPlayer['name'], "will be playing X today, and gets to pick the first spot on the board")
    board = ['', '', '', '', '', '', '', '', '']
    options = ['rock', 'scissors', 'paper', 'lizard', 'spock']
    print_board(board)
    while True:
        while True:
            print(currentPlayer['name'], "where would you like to place your", currentPlayer['piece'])
            row = int(input("Row: "))
            while row > 3 or row < 1:
                print("Sorry wrong input. Please try again")
                row = int(input("Row: "))
            column = int(input("Column: "))
            while column > 3 or column < 1:
                print("Sorry wrong input. Please try again")
                column = int(input("Column: "))
                print(check_if_vacant(board, row, column))
            if check_if_vacant(board, row, column):
                break
            else:
                print("That spot is filled. Please choose another one")
        print("In order to win your square you must win a game of Rock, Scissors,Paper, Lizard, Spock!")
        userselection = str(input('{} pick one of Rock, Scissors,Paper, Lizard, Spock!: '.format(currentPlayer['name'])))
        while userselection.lower() not in options:
            print("I am sorry, that is an invalid option. Lets try again")
            userselection = str(
                input('{} pick one of Rock, Scissors,Paper, Lizard, Spock!: '.format(currentPlayer['name'])))
        userselection = userselection.lower()
        computer_selection = options[random.randint(0, 4)]
        while computer_selection == userselection:
            computer_selection = options[random.randint(0, 4)]
        print('Our celebrity guest picked {}. '.format(computer_selection), end='')
        winner = selection_winner(userselection, computer_selection)
        if winner['win']:
            print('{}, {}, you win the square!'.format(winner['message'], currentPlayer['name']))
            board[get_board_number(row, column)] = currentPlayer['piece']
        else:
            print('{}, I\'m Sorry {}, you lost the square!'.format(winner['message'], currentPlayer['name']))
            temp_board = board.copy()
            if currentPlayer['piece'] == 'x':
                temp_board[get_board_number(row, column)] = 'o'
                if not check_if_won(temp_board, 'o'):
                    board = temp_board.copy()
            else:
                temp_board[get_board_number(row, column)] = 'x'
                if not check_if_won(temp_board, 'x'):
                    board = temp_board.copy()
        print_board(board)
        print('-' * 100)
        if check_if_won(board, currentPlayer['piece']):
            print(currentPlayer['name'], "won with piece", currentPlayer['piece'])
            break
        if currentPlayer['name'] == player1['name']:
            currentPlayer = player2
        else:
            currentPlayer = player1
        if not any(x == '' for x in board):
            print("Sorry its a draw")
            break
    playagain = input("Would you like to play again? (yes/no)")
    if playagain == 'yes':
        playgame()

playgame()
