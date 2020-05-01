
# testing sudoku board
test_board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# creating a printing function to better visualise the sudoku table when printing out
def print_board(board):
    for i in range(len(board)): # going through the rows in the array, look for the third row and print separating line
        if i % 3 == 0 and i != 0: # for every third row, print a separating line
            print("- - - - - - - - - -")
        for j in range(len(board[0])): # going through each individual element in the row
            if j % 3 == 0 and j != 0: # for every third element, print a separating line
                print("|", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# creating a function to find if that element in the array is 0 or "empty"
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # returns a tuple of row, col
    return None


# creating a function that validates if the element in that spot is valid or not
def validate(board, number, position): # pass in the current board array, the number to be validated, and a tuple of the position of the empty space
    row = position[0]
    col = position[1]

    # check in the row
    for i in range(len(board[row])):
        if not i == col and board[row][i] == number:
            return False

    # check in the column
    for j in range(len(board)):
        if not j == row and board[j][col] == number:
            return False

    # finding the index of the subgrid
    subgrid_y = row // 3 # to find the row index of the subgrid the value is in
    subgrid_x = col //3 # to find the col index of the subgrid the value is in
    # checking in the subgrid
    for m in range(subgrid_y*3, subgrid_y*3+3):
        for n in range(subgrid_x*3, subgrid_x*3+3):
            if m != row and n != col and board[m][n] == number:
                return False

    # if the number in the position is valid, return True
    return True


# creating a recursive function that loops over every element in the sudoku board until a solution is reached
def solve(board):
    if find_empty(board) is None:
        return True
    else:
        row, col = find_empty(board)

    for i in range(1,10): # loops through values 1 to 9 and input into the empty spot for validation
        if validate(board, i, (row,col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

print_board(test_board)
print("\n")
solve(test_board)
print_board(test_board)