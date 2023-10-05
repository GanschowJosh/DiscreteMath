"""
Prove that for any 2^n by 2^n grid with any one square removed, a number of L-shaped triominoes can be made to cover it
Proven visually by taking input from the user for board size and using matplotlib to visualize the constructed board,
and it will also print out the board into the terminal so the user can copy it if they want to use it 
in a different way.
It will also print out the number of triominoes required to cover the board
"""


import numpy as np
import matplotlib.pyplot as plt

# Function to create the initial board with a missing square
def create_board(size, missing_square):
    # Create a size x size board filled with zeros
    board = np.zeros((size, size), dtype=int)
    # Mark the missing square with -1
    board[missing_square[0], missing_square[1]] = -1
    return board

def print_board_terminal(board):
    size = len(board)
    for i in range(size):
        for j in range(size):
            if board[i, j] == -1:
                print(" X ", end="")
            elif board[i, j] == 0:
                print(" . ", end="")
            else:
                # Print the tile_id modulo 100 with a fixed width of 3 to align the columns
                print(f"{board[i, j] % 100:3}", end="")
        print()
    print(f"{board[size-1][size-1]} is the number of triominoes required to cover the board")

# Function to print the board using matplotlib for a more visually appealing output
def print_board(board):
    fig, ax = plt.subplots()
    ax.imshow(board, cmap='nipy_spectral')  # Use a colormap with a wide range of colors

    # Loop over the board and add labels to the squares
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i, j] == -1:  # If the square is missing, mark it with 'X'
                ax.text(j, i, 'X', ha='center', va='center', color='black')
            elif board[i, j] != 0:  # If the square is covered by a tile, label it with the tile number
                ax.text(j, i, str(board[i, j] % 100), ha='center', va='center', color='black')

    plt.show()  # Display the plot
    print_board_terminal(board)

# Global variable to keep track of the current tile number
tile_id = 1

# Function to cover the board with L-shaped tiles
def cover_board(board, size, row, col, missing_square):
    global tile_id  # Use the global tile_id variable
    if size == 2:
        # Base case: place a single triomino (L-shaped tile)
        triomino = [(0, 0), (0, 1), (1, 0), (1, 1)]
        if (missing_square[0] - row, missing_square[1] - col) in triomino:
            triomino.remove((missing_square[0] - row, missing_square[1] - col))
        for dx, dy in triomino:
            board[row + dx][col + dy] = tile_id
        tile_id += 1
        return

    sub_size = size // 2  # Size of each quadrant

    # Find the quadrant of the missing square
    quadrant = 0
    if missing_square[0] >= row + sub_size:
        quadrant += 2
    if missing_square[1] >= col + sub_size:
        quadrant += 1

    # Define the offsets for each quadrant
    offsets = [(0, 0), (0, sub_size), (sub_size, 0), (sub_size, sub_size)]

    # Place a triomino in the center of the board covering three quadrants
    center_triominos = [(sub_size - 1, sub_size - 1), (sub_size - 1, sub_size),
                        (sub_size, sub_size - 1), (sub_size, sub_size)]
    del center_triominos[quadrant]
    
    for dx, dy in center_triominos:
        board[row + dx][col + dy] = tile_id
    tile_id += 1

    # Recursively cover each quadrant
    new_missing_squares = [(row + center_triominos[i][0], col + center_triominos[i][1]) for i in range(3)]
    new_missing_squares.insert(quadrant, missing_square)
    
    for i in range(4):
        dx, dy = offsets[i]
        cover_board(board, sub_size, row + dx, col + dy,
                    new_missing_squares[i])

# Main function to run the program
def main():
    global tile_id
    
    # Get user input for board size and location of missing square
    size = int(input("Enter the board size (2^n): "))
    missing_row = int(input("Enter the row of the missing square: "))
    missing_col = int(input("Enter the column of the missing square: "))
    
    missing_square = (missing_row, missing_col)

    if size <= 0 or missing_row < 0 or missing_row >= 2 ** size or missing_col < 0 or missing_col >= 2 ** size:
        print("Invalid input!")
        return

    # Create and cover the board
    board = create_board(2 ** size, missing_square)
    
    tile_id = 1
    
    cover_board(board, 2 ** size, 0, 0, missing_square)
    
    print_board(board)   # Print the covered board

if __name__ == "__main__":
   main()
