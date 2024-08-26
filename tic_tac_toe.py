def print_board(board):
    """Print the current state of the board."""
    print("---------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("---------")


def check_winner(board):
    """Check if there is a winner or the game is a draw."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    # Check for draw
    if all(board[row][col] != ' ' for row in range(3) for col in range(3)):
        return 'Draw'

    return None


def get_move(player):
    """Get the next move from the player."""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move >= 1 and move <= 9:
                return move
            else:
                print("Invalid move. Enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


def play_game():
    """Main function to play the game."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        move = get_move(current_player)

        # Convert move (1-9) to board indices
        row = (move - 1) // 3
        col = (move - 1) % 3

        if board[row][col] != ' ':
            print("The cell is already occupied. Try again.")
            continue

        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == 'Draw':
                print("It's a draw!")
            else:
                print(f"Player {winner} wins!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_game()