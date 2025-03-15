import random

def initialize_board(size=4):
    """Initializes the game board with two random tiles."""
    board = [[0] * size for _ in range(size)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    """Adds a new tile (2 or 4) to a random empty cell on the board."""
    empty_cells = [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4

def transpose(board):
    """Transposes the board (rows become columns and vice versa)."""
    return [list(row) for row in zip(*board)]

def reverse(board):
    """Reverses each row of the board."""
    return [row[::-1] for row in board]

def merge_left(board):
    """Merges tiles to the left."""
    board_changed = False
    for row in board:
        # Remove zeros
        row_no_zeros = [x for x in row if x != 0]
        # Merge equal adjacent tiles
        merged_row = []
        i = 0
        while i < len(row_no_zeros):
            if i + 1 < len(row_no_zeros) and row_no_zeros[i] == row_no_zeros[i + 1]:
                merged_row.append(row_no_zeros[i] * 2)
                i += 2
                board_changed = True
            else:
                merged_row.append(row_no_zeros[i])
                i += 1
        # Add zeros to the end
        merged_row += [0] * (len(row) - len(merged_row))
        # Update the row
        for i in range(len(row)):
            row[i] = merged_row[i]
    return board, board_changed

def move_left(board):
    """Moves tiles to the left."""
    board, board_changed = merge_left(board)
    return board, board_changed

def move_right(board):
    """Moves tiles to the right."""
    board = reverse(board)
    board, board_changed = merge_left(board)
    board = reverse(board)
    return board, board_changed

def move_up(board):
    """Moves tiles up."""
    board = transpose(board)
    board, board_changed = merge_left(board)
    board = transpose(board)
    return board, board_changed

def move_down(board):
    """Moves tiles down."""
    board = transpose(board)
    board = reverse(board)
    board, board_changed = merge_left(board)
    board = reverse(board)
    board = transpose(board)
    return board, board_changed

def print_board(board):
    """Prints the board to the console."""
    for row in board:
        print(" ".join(str(x).center(4) for x in row))

def game_over(board):
    """Checks if the game is over."""
    for row in board:
        for x in row:
            if x == 0:
                return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i + 1 < len(board) and board[i][j] == board[i + 1][j]:
                return False
            if j + 1 < len(board[0]) and board[i][j] == board[i][j + 1]:
                return False
    return True

def play_game():
    """Plays the 2048 game."""
    board = initialize_board()
    print("Welcome to 2048!")
    print("Use 'w', 'a', 's', 'd' to move up, left, down, right respectively.")
    print("Enter 'q' to quit.")

    while not game_over(board):
        print_board(board)
        move = input("Enter your move: ").lower()

        if move == 'w':
            board, board_changed = move_up(board)
        elif move == 'a':
            board, board_changed = move_left(board)
        elif move == 's':
            board, board_changed = move_down(board)
        elif move == 'd':
            board, board_changed = move_right(board)
        elif move == 'q':
            print("Quitting the game.")
            break
        else:
            print("Invalid move. Please use 'w', 'a', 's', 'd', or 'q'.")
            continue

        if board_changed:
            add_new_tile(board)
        else:
            print("No change on the board.")

    if game_over(board):
        print_board(board)
        print("Game over!")

# Start the game
if __name__ == "__main__":
    play_game()