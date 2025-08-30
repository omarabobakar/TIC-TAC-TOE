

# Tic Tac Toe with AI (Minimax with Alpha-Beta Pruning)

# Function to print the board
def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(" " + board[i][j] + " ", end="|")
        print("\n-------------")

# Function to check for a winning condition
def check_win(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check if the game is over
def game_over(board):
    return check_win(board, "X") or check_win(board, "O") or not any(" " in row for row in board)

# Function to evaluate the board for the AI player
def evaluate(board):
    if check_win(board, "X"):
        return 1
    elif check_win(board, "O"):
        return -1
    else:
        return 0

# Minimax function with alpha-beta pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    if game_over(board) or depth == 0:
        return evaluate(board)

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval_score = minimax(board, depth - 1, alpha, beta, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval_score)
                    alpha = max(alpha, eval_score)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval_score = minimax(board, depth - 1, alpha, beta, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval_score)
                    beta = min(beta, eval_score)
                    if beta <= alpha:
                        break
        return min_eval

# Function to make the AI's move
def make_ai_move(board):
    best_eval = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                eval_score = minimax(board, 6, float('-inf'), float('inf'), False)
                board[i][j] = " "
                if eval_score > best_eval:
                    best_eval = eval_score
                    best_move = (i, j)

    board[best_move[0]][best_move[1]] = "X"

# Function to play the game
def play_game():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    current_player = "O"
    game_over = False

    while not game_over:
        if current_player == "O":
            print_board(board)
            row = int(input("Enter the row number (0, 1, or 2): "))
            col = int(input("Enter the column number (0, 1, or 2): "))
            if board[row][col] == " ":
                board[row][col] = current_player
                if check_win(board, current_player):
                    print_board(board)
                    print("Player", current_player, "wins!")
                    game_over = True
                elif " " not in board[0] and " " not in board[1] and " " not in board[2]:
                    print_board(board)
                    print("It's a tie!")
                    game_over = True
                else:
                    current_player = "X"
            else:
                print("Invalid move. That spot is already taken.")
        else:
            make_ai_move(board)
            if check_win(board, current_player):
                print_board(board)
                print("Player", current_player, "wins!")
                game_over = True
            elif " " not in board[0] and " " not in board[1] and " " not in board[2]:
                print_board(board)
                print("It's a tie!")
                game_over = True
            else:
                current_player = "O"

# Start the game
play_game()
