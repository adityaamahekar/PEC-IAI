board = [' '] * 9

def show():
    for i in range(0, 9, 3):
        print(board[i:i+3])

def win(p):
    lines = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(all(board[i] == p for i in line) for line in lines)

for turn in range(9):
    show()
    p = 'X' if turn % 2 == 0 else 'O'

    while True:
        try:
            pos = int(input(f"{p} enter position (1-9): ")) - 1
            if 0 <= pos < 9 and board[pos] == ' ':
                break
        except ValueError:
            pass
        print("Invalid position. Try again.")

    board[pos] = p

    if win(p):
        show()
        print(p, "wins!")
        break
else:
    show()
    print("Draw!")