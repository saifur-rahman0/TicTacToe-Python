import random
import os.path
import json
import sys

random.seed()

score = 0
def draw_board(board):
    print("\t-------------")
    print("\t| %c | %c | %c |" % (board[1], board[2], board[3]))
    print("\t-------------")
    print("\t| %c | %c | %c |" % (board[4], board[5], board[6]))
    print("\t-------------")
    print("\t| %c | %c | %c |" % (board[7], board[8], board[9]))
    print("\t-------------")


def welcome(board):
    print("Welcome to the \"Unbeatable Noughts and Crosses\" game.")
    draw_board(board)


def initialise_board(board):
    for i in range(10):
        board[i]= ' '
    return board


def get_player_move(board):
    while True:
        try:
            print("                    1 2 3")
            print("                    4 5 6")
            position = int(input("Choose your square: 7 8 9 :"))
            if 1 <= position <= 9:
                if board[position] == ' ':
                    return position
                else:
                    print("Cell already occupied. Try again.")
            else:
                print("Invalid input. Enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Enter a number.")


def choose_computer_move(board):
    empty_cells = [(i) for i in range(9) if board[i] == ' ' and i != 0]
    return random.choice(empty_cells)


def check_for_win(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark and board[1] != ' ':
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark and board[4] != ' ':
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark and board[7] != ' ':
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark and board[1] != ' ':
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark and board[2] != ' ':
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark and board[3] != ' ':
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark and board[5] != ' ':
        return True
    elif board[3] == mark and board[5] == mark and board[7]== mark and board[5] != ' ':
        return True
    return False


def check_for_draw(board):
    if board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        return True


def play_game(board):
    global score
    initialise_board(board)
    draw_board(board)
    while True:
        position = get_player_move(board)
        board[position] = 'X'
        print()
        draw_board(board)

        if check_for_win(board, 'X'):
            score += 1
            print("You won the game.")
            break

        if check_for_draw(board):
            print("Draw the game.")
            break

        ccm= choose_computer_move(board)
        print("Computer choose the square: %d" % (ccm))
        board[ccm] = 'O'
        draw_board(board)

        if check_for_win(board, 'O'):
            score -=1
            break

        if check_for_draw(board):
            break
    return score

def menu():
    print("Enter one of the following options:")
    print("1 - Play the game")
    print("2 - Save your score in the leaderboard")
    print("3 - Load and display the leaderboard")
    print("q - End the program")
    choice = input("1, 2, 3, q? ")
    return choice


def load_scores():
    leaders = {}
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt", "r") as file:
            try:
                leaders = json.load(file)
            except json.JSONDecodeError:
                print("Error decoding JSON. Returning empty leaderboard.")
    return leaders

def save_score(score):
    player_name = input("Enter your name: ")
    leaders = load_scores()
    leaders[player_name] = score
    with open("leaderboard.txt", "w") as file:
        json.dump(leaders, file)


def display_leaderboard(leaders):
    print("Leaderboard:")
    for player, score in leaders.items():
        print(f"{player}: {score}")


if __name__ == "__main__":
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    while True:
        choice = menu()
        if choice == '1':
            score = play_game(board)
        elif choice == '2':
            save_score(score)
        elif choice == '3':
            leaders = load_scores()
            display_leaderboard(leaders)
        elif choice == 'q':
            sys.exit()
        else:
            print("Invalid choice. Please choose again.")
