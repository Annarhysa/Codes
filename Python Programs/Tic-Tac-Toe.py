import random

board = [[' ']*3 for _ in range(3)]
players = ["X", "O"]
current_player = random.choice(players)

def display_board():
    print('\n'.join(['|'.join(row) for row in board]))

def check_win():
    rows = board
    cols = [[board[j][i] for j in range(3)] for i in range(3)]
    diags = [[board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]]
    lines = rows + cols + diags
    return any([all([cell == current_player for cell in line]) for line in lines])

while True:
    print("Player", current_player, "make your move.")
    display_board()
    row = int(input("Enter the row (1-3): ")) - 1
    col = int(input("Enter the column (1-3): ")) - 1
    
    if board[row][col] == ' ':
        board[row][col] = current_player
        if check_win():
            print("Player", current_player, "wins!")
            break
        elif all([cell != ' ' for row in board for cell in row]):
            print("It's a tie!")
            break
        else:
            current_player = "X" if current_player == "O" else "O"
    else:
        print("Position already taken. Try again.")
