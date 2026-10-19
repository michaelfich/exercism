CHESS_BOARD_SQUARES = 64

def square(number):
    if number < 1 or number > CHESS_BOARD_SQUARES:
        raise ValueError("square must be between 1 and 64")

    return 2 ** (number - 1)


def total():
    total_squares = 0
    for number in range(1, CHESS_BOARD_SQUARES + 1):
        total_squares = total_squares + square(number)
    return total_squares
