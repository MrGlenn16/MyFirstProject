# My board
Board = {'a': {1: ' ', 2: ' ', 3: ' '}, 'b': {4: ' ', 5: ' ', 6: ' '}, 'c': {7: ' ', 8: ' ', 9: ' '}}

# Placeholder lists
Available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
possibleSigns = ["o", "x"]
mov_played = ["a"]
X_win = ['x', 'x', 'x']
O_win = ['o', 'o', 'o']

# Flags
activation_flag = True


# Stupid Function to print the board
def board():
    print(Board['a'])
    print(Board['b'])
    print(Board['c'])


# Function to pick the position
def picking_position(number, sign):
    if number in Available:
        Available[number - 1] = 'Taken'
        if 0 < number <= 3:
            Board['a'][number] = sign

        elif 3 < number <= 6:
            Board['b'][number] = sign

        elif 6 < number <= 9:
            Board['c'][number] = sign
    else:
        print('Already chosen, pick another')
        pass


# Functions to determine the winner

def row_checker(row):
    if list(Board[row].values()) == X_win or list(Board[row].values()) == O_win:
        print(f"{mov_played[-1]} just won!")
        global activation_flag
        activation_flag = False


def column_checker():
    column1 = [Board['a'][1], Board['b'][4], Board['c'][7]]
    column2 = [Board['a'][2], Board['b'][5], Board['c'][8]]
    column3 = [Board['a'][3], Board['b'][6], Board['c'][9]]
    if column1 == X_win or column2 == X_win or column3 == X_win:
        print("x just won!")
        global activation_flag
        activation_flag = False
    elif column1 == O_win or column2 == O_win or column3 == O_win:
        print("o just won!")
        activation_flag = False


def diagonals_checker():
    diagonal1 = [Board['a'][1], Board['b'][5], Board['c'][9]]
    diagonal2 = [Board['a'][3], Board['b'][5], Board['c'][7]]
    if diagonal1 == X_win or diagonal2 == X_win:
        print("x just won!")
        global activation_flag
        activation_flag = False
    elif diagonal1 == O_win or diagonal2 == O_win:
        print("o just won!")
        activation_flag = False


# Board printed for the first time
board()

# Actual game
while activation_flag:
    firstQ = int(input("What position do u wanna play? (1-9): "))
    secondQ = str(input("What sign are u? (X/O): "))

    if firstQ not in range(1, 10):
        print("You are out of range, pick one number from 1 to 9")
    elif secondQ not in possibleSigns:
        print("You can only choose X or O")
    elif secondQ == mov_played[-1]:
        print("It's not your turn")
    elif len(mov_played) > 10:
        print("Nobody Won!")
        break
    else:
        picking_position(firstQ, secondQ)
        board()
        mov_played.append(secondQ)
        row_checker('a')
        row_checker('b')
        row_checker('c')
        column_checker()
        diagonals_checker()
