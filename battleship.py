''' File: battleship.py
    Desc: Battleship game as cli program '''

from random import randint


def main():
    board = []
    for x in range(5):
        board.append(["O"] * 5)  # make a list of lists
    print('----------------------')
    print('Let\'s play Battleship')
    render_gameboard(board)

    ship_row = randint(0, len(board) - 1)
    ship_col = randint(0, len(board[0]) - 1)
    ship_position = [ship_row, ship_col]
    # print(f'{ship_position} is a type of {type(ship_position)}')  # list

    # gameplay (6 chances)
    for guesses in range(6):
        print(f"You have {6 - guesses} guesses left...")
        guess = input(
            "Guess the position of the battleship by entering a row,col: ")

        print(f'debug: here is the ship position: {ship_position}')

        # hit and sink!
        if int(guess[0]) == ship_position[0] and int(guess[1]) == ship_position[1]:
            print("Congrats! You sunk the opponent's 1x1 tugboat battleship!")
            board[int(guess[0])][int(guess[1])] = "*"
            break

        # miss and other mis-adventures
        else:
            # check for out of bounds - here manual # TODO: use > range()
            if int(guess[0]) < 0 or int(guess[0]) > 4 or int(guess[1]) < 0 or int(guess[1]) > 4:
                print("Oops! that's out of bounds fool. Guess Again!")
                render_gameboard(board)
            # check if position has already been guessed
            elif board[int(guess[0])][int(guess[1])] == "X":
                print("You guessed that one already fool. Guess Again!")
                render_gameboard(board)
            # you missed (mark the spot with an X)
            else:
                print("You missed the battleship")
                board[int(guess[0])][int(guess[1])] = "X"
                render_gameboard(board)

        if guesses == 5:
            print("GAME OVER")
            print(f'The battleship position was hiding at: {ship_position}')
    # print the final game board
    render_gameboard(board)


def render_gameboard(board):
    for row in board:
        print(("  ").join(row))


if __name__ == "__main__":
    main()
