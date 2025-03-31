BOARDWIDTH = 3
BOARDHEIGHT = 3
BLANK = None

counter = 1
board = []
for x in range(BOARDWIDTH):
    column = []
    for y in range(BOARDHEIGHT):
        column.append(counter)
        counter += BOARDWIDTH
    board.append(column)
    counter -= BOARDWIDTH * (BOARDHEIGHT - 1) + BOARDWIDTH - 1

board[BOARDWIDTH-1][BOARDHEIGHT-1] = BLANK
print(board) 

counter = 0
board = []
for x in range(BOARDWIDTH):
    counter = x + 1
    column = []
    for y in range(BOARDHEIGHT):
        # print(counter)
        column.append(counter)
        counter += BOARDWIDTH
    # print('When x is {}\t counter is :{}'.format(x,counter))
    board.append(column)
    
board[BOARDWIDTH-1][BOARDHEIGHT-1] = BLANK
print(board) 