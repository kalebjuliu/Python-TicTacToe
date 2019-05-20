game = [[1,1,1],
        [1,1,0],
        [1,0,0]]

'''
00 11 22
02 11 20
'''


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map

    except IndexError as e:
        print("Error: Insert row/column value between 0 and 2", e)
    except Exception as e:
        print("Something went wrong")

def horizontal_win(current_game):
    for row in current_game:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("Winner")

def vertical_win(current_game):
    check = []
    for row in current_game:
        check.append(row[0])
    if check.count(check[0]) == len(check) and check[0] != 0:
        print("Winner")


def diag_win(current_game):
    diags = []
    for ix in range(len(current_game)):
        diags.append(current_game[ix][ix])
    print(diags)


def diag_win_1(current_game):
    diags = []
    for row, col in enumerate(reversed(range(len(current_game)))):
        diags.append(current_game[row][col])
    print(diags)


game = game_board(game, just_display=True)

horizontal_win(game)
vertical_win(game)
diag_win(game)
diag_win_1(game)

