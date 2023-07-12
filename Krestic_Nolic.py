# Крестики нолики
print("Крестики нолики версия 1.0")
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Доска
def draw_board(board):
    print("*" * 6)
    for i in range(3):
        print(board[i + 0 * 3], board[i + 1 * 3], board[i + 2 * 3])
        print("*" * 6)
# Ввод данных
def input_player(player):
    while True:
        hod_1 = input("Введите число" + player + ":")
        if len(hod_1) != 1:
            print("Введите пожалуйста число!")
            continue
        hod_1 = int(hod_1)
        if str(board[hod_1 - 1]) in "XO":
            print("Эта клетка уже занята")
            continue
        board[hod_1 - 1] = player
        break
def win():
    winner = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (7, 5, 3)]
    for i in winner:
        if board[i[0]-1] == board[i[1]-1] == board[i[2]-1]:
            return board[i[1] - 1]
    else:
        return False


# Функция чтоб все работало на конец то !!!!
def main(board):
    count = 0
    while True:
        draw_board(board)
        if count % 2 == 0:
            input_player("X")
        else:
            input_player("O")
        if count > 3:
            wins = win()
            if wins:
                draw_board(board)
                print(wins , "Победа ")
                break
        count += 1
        if count > 8:
            wins = win()
            if wins:
                draw_board(board)
                print(wins, "Ничья ")
                break

main(board)


