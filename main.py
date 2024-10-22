from __future__ import annotations

from tictactoe.tictactoe import check_win_condition
from tictactoe.tictactoe import create_board
from tictactoe.tictactoe import place
from tictactoe.tictactoe import show_board_state


def main():
    """Where the main game loop is run"""
    board = create_board()
    turn_number = 0
    while True:
        turn_number += 1
        print(f"\nTurn {turn_number} board state:")

        show_board_state(board)

        x = int(input("Enter X coordinate: "))
        y = int(input("Enter Y coordinate: "))

        board = place(board, x, y, turn_number)

        if check_win_condition(board):
            if turn_number % 2 != 0:
                show_board_state(board)
                print("     X wins!")
            else:
                show_board_state(board)
                print("     O wins!")
            break


if __name__ == "__main__":
    main()
