from __future__ import annotations


def create_board() -> list[list[str]]:
    """Creates the initial array to be used as the board

    Returns:
        list[list[str]]: Initial board array
    """
    return [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"],
    ]


def place(
    board: list[list[str]],
    x: int,
    y: int,
    turn_number: int,
) -> list[list[str]]:
    """Places an X or O on the board in a specified place, uses recursion to
        avoid placing pieces on occupied spaces

    Arguments:
        board:              Current board state
        x:                  X coordinate
        y:                  Y coordinate
        turn_number:        The current turn number

    Returns:
        list[list[str]]:    New board state
    """
    if turn_number % 2 != 0:
        if board[x][y] == "-":
            board[x][y] = "X"
        else:
            print("\nSpace already occupied, try again\n")
            place(
                board,
                int(input("Enter Y coordinate: ")),
                int(input("Enter X coordinate: ")),
                turn_number,
            )
    else:
        if board[x][y] == "-":
            board[x][y] = "O"
        else:
            print("\nSpace already occupied, try again\n")
            place(
                board,
                int(input("Enter Y coordinate: ")),
                int(input("Enter X coordinate: ")),
                turn_number,
            )

    return board


def show_board_state(board):
    """Prints the current board state

    Arguments:
    board: Current board state
    """
    print(" ")

    for i in range(len(board)):
        print("     ", board[0][i], board[1][i], board[2][i])

    print(" ")


def check_win_condition(board: list[list[str]]) -> bool:
    """Checks the board for completed lines

    Arguments:
        board:  Current board state

    Returns:
    bool:   Whether a complete line has been found
    """
    for i in range(len(board)):
        if board[i].count(board[i][0]) == len(board[0]) and board[i][0] != "-":
            return True
    for i in range(len(board)):
        if all(col[i] == board[0][i] for col in board) and board[0][i] != "-":
            return True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "-":
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != "-":
        return True
    return False
