import chess

# Initialize a chess board
board = chess.Board()

# Function to display the chess board
def display_board(board):
    print(board)

# Main game loop
while not board.is_game_over():
    display_board(board)
    
    # Get player's move input
    move = input("Enter your move (e.g., 'e2 e4'): ")
    
    try:
        # Try to make the move on the board
        board.push_san(move)
    except ValueError:
        print("Invalid move. Try again.")
        continue

# Game result
if board.is_checkmate():
    print("Checkmate! Game over.")
elif board.is_stalemate():
    print("Stalemate! Game over.")
elif board.is_insufficient_material():
    print("Insufficient material. Game over.")
elif board.is_seventyfive_moves():
    print("Draw due to 75-move rule. Game over.")
elif board.is_fivefold_repetition():
    print("Draw due to fivefold repetition. Game over.")
elif board.is_variant_draw():
    print("Draw due to specific chess variant rules. Game over.")
else:
    print("Game ended for some other reason.")
