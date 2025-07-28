def print_board(board):
    """Prints the current state of the Tic-Tac-Toe board."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    """Checks if the given player has won the game."""
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True
    return False

def check_draw(board):
    """Checks if the game is a draw."""
    return " " not in board

def get_player_move(player, board):
    """Gets a valid move from the current player."""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
            else:
                print("Invalid move. That spot is either taken or out of range. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def play_game():
    """Manages the main game loop for Tic-Tac-Toe."""
    board = [" " for _ in range(9)]  # Initialize empty board
    current_player = "X"
    game_over = False

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not game_over:
        move = get_player_move(current_player, board)
        board[move] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(f"Congratulations! Player {current_player} wins!")
            game_over = True
        elif check_draw(board):
            print("It's a draw!")
            game_over = True
        else:
            # Switch player
            current_player = "O" if current_player == "X" else "X"

    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()