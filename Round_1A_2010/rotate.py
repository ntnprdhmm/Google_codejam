""" Return true if the char in parameter is R or B
"""
def is_valid_letter(c):
    return c== 'R' or c == 'B'

""" Get all the valid letters of an array passed in parameter
"""
def get_col_letters(col, n):
    letters = []
    for i in range(n):
        if is_valid_letter(col[i]):
            letters.append(col[i])
    return letters

""" Print the board in the console
"""
def print_board(board, n):
    for r in range(n):
        row = ""
        for c in range(n):
            row += board[r][c]
        print(row)

f_name = "A-large-practice"
f_in = open(f_name + ".in", "r")
f_out = open(f_name + ".out", "w")

# for each test case
for test_case in range(int(f_in.readline().strip())):
    # n = the board size, k = the number to align
    n, k = list(map(int, f_in.readline().strip().split()))
    board = [['x' for _ in range(n)] for _ in range(n)]
    # read the board, but rotate it and apply gravity in the same time (read a line but put it as a col)
    for line in range(n):
        col = f_in.readline().strip()
        # apply gravity => shift all to the right
        letters = get_col_letters(col, n)
        col = ['.'] * (n - len(letters)) + letters
        # update the col in board
        for i in range(n):
            board[i][n - 1 - line] = col[i]
    # search the alignments for each player
    players = {
        'R': False,
        'B': False
    }
    j = 0
    while j < n and (not players['R'] or not players['B']):
        i = 0
        while i < n and (not players['R'] or not players['B']):
            if (board[j][i] == 'R' or board[j][i] == 'B') and not players[board[j][i]]:
    
                # bottom check
                m = 1
                while j + m < n and board[j+m][i] == board[j][i]:
                    m += 1
                if m >= k:
                    players[board[j][i]] = True

                # right check
                if not players[board[j][i]]:
                    m = 1
                    while i + m < n and board[j][i+m] == board[j][i]:
                        m += 1
                    if m >= k:
                        players[board[j][i]] = True
                
                # left diagonal
                if not players[board[j][i]]:
                    m = 1
                    while j + m < n and i - m >= 0 and board[j+m][i-m] == board[j][i]:
                        m += 1
                    if m >= k:
                        players[board[j][i]] = True

                # right diagonal
                if not players[board[j][i]]:
                    m = 1
                    while j + m < n and i + m < n and board[j+m][i+m] == board[j][i]:
                        m += 1
                    if m >= k:
                        players[board[j][i]] = True

            i += 1
        j += 1
                
    # print the result
    result = "Neither"
    if players['R']:
        if players['B']:
            result = "Both"
        else:
            result = "Red"
    elif players['B']:
        result = "Blue"

    f_out.write("Case #{}: {}\n".format(test_case+1, result))