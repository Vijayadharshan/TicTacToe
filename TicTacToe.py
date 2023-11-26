player1 = 1
player2 = 2


def print1(matrix):
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()


def check_win(matrix, player, check_filled):
    # Check rows
    for i in matrix:
        if all(j == player for j in i):
            print(f'Player {player} wins')
            return True

    # Check columns
    for i in range(len(matrix)):
        if all(matrix[j][i] == player for j in range(len(matrix))):
            print(f'Player {player} wins')
            return True

    # Check diagonals
    diagonal1 = [matrix[i][i] for i in range(len(matrix))]
    diagonal2 = [matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]
    if all(i == player for i in diagonal1) or all(i == player for i in diagonal2):
        print(f'Player {player} wins')
        return True

    if len(check_filled) == 9:
        return True

    return False


game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

print1(game)

filled = set()
win = False
while not win:

    x = int(input('Player 1: '))
    row = (x - 1) // len(game[0])
    col = (x - 1) % len(game[0])

    if 1 <= x <= 9 and x not in filled:
        game[row][col] = player1
        filled.add(x)
    else:
        print('Invalid Response')
        break

    print1(game)
    win = check_win(game, player1, filled)

    if win:
        break

    y = int(input('Player 2: '))

    row = (y - 1) // len(game[0])
    col = (y - 1) % len(game[0])

    if 1 <= y <= 9 and y not in filled:
        game[row][col] = player2
        filled.add(y)
    else:
        print('Invalid Response')
        break

    print1(game)
    win = check_win(game, player2, filled)

    if win:
        break
