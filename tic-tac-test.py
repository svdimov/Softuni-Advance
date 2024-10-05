# Tic-Tac-Toe game implementation in Python

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()



def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


# Function to check if the board is full (tie)
def check_tie(board):
    return all([spot != " " for spot in board])


# Function to play the game
def play_game():
    board = [" " for _ in range(9)]  # Initialize empty board
    current_player = "X"  # Player X always starts

    while True:
        print_board(board)
        # Get valid player input
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

        if board[move] != " ":
            print("Invalid move! Spot already taken. Try again.")
            continue

        # Make the move
        board[move] = current_player

        # Check if the current player won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a tie
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"


# Start the game
if __name__ == "__main__":
    play_game()
