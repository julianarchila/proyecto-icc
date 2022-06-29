def main():
    import random

    board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]  # recuerda que el y va de primero
    userpress = "q"


    def boardprint(board):
        print(board[0])
        print(board[1])
        print(board[2])
        print(board[3])


    def placenewtwo(board):
        placex = random.randint(0, 3)
        placey = random.randint(0, 3)
        while board[placey][placex] != 0:
            placex = random.randint(0, 3)
            placey = random.randint(0, 3)
        board[placey][placex] = 2


    def mergeright(board):
        tempplacey = 3
        tempplacex = 2
        while tempplacey >= 0 and tempplacex >= 0:
            while tempplacey >= 0:
                if board[tempplacey][tempplacex] > 0:
                    if (
                        board[tempplacey][3] == board[tempplacey][tempplacex]
                        and tempplacex < 3
                    ):
                        board[tempplacey][3] = board[tempplacey][tempplacex] * 2
                        board[tempplacey][tempplacex] = 0
                    elif (
                        board[tempplacey][2] == board[tempplacey][tempplacex]
                        and tempplacex < 2
                    ):
                        board[tempplacey][2] = board[tempplacey][tempplacex] * 2
                        board[tempplacey][tempplacex] = 0
                    elif (
                        board[tempplacey][1] == board[tempplacey][tempplacex]
                        and tempplacex < 1
                    ):
                        board[tempplacey][1] = board[tempplacey][tempplacex] * 2
                        board[tempplacey][tempplacex] = 0
                tempplacey = tempplacey - 1
            tempplacex = tempplacex - 1
            tempplacey = 3


    def moveright(board):
        mergeright(board)
        tempplacey = 3
        tempplacex = 2
        while tempplacey >= 0 and tempplacex >= 0:
            while tempplacey >= 0:
                if board[tempplacey][tempplacex] > 0:
                    if board[tempplacey][3] == 0:
                        board[tempplacey][3] = board[tempplacey][tempplacex]
                        board[tempplacey][tempplacex] = 0
                    elif board[tempplacey][2] == 0 and tempplacex < 3:
                        board[tempplacey][2] = board[tempplacey][tempplacex]
                        board[tempplacey][tempplacex] = 0
                    elif board[tempplacey][1] == 0 and tempplacex < 2:
                        board[tempplacey][1] = board[tempplacey][tempplacex]
                        board[tempplacey][tempplacex] = 0
                tempplacey = tempplacey - 1
            tempplacex = tempplacex - 1
            tempplacey = 3


    def mergeleft(board):
        tempplacey = 3
        tempplacex = 1
        while tempplacey >= 0 and tempplacex <= 3:
            while tempplacey >= 0:
                if board[tempplacey][tempplacex] > 0:
                    if (
                        board[tempplacey][0] == board[tempplacey][tempplacex]
                        and tempplacex > 0
                    ):
                        board[tempplacey][0] = board[tempplacey][tempplacex] * 2
                        board[tempplacey][tempplacex] = 0
                    elif (
                        board[tempplacey][1] == board[tempplacey][tempplacex]
                        and tempplacex > 1
                    ):
                        board[tempplacey][1] = board[tempplacey][tempplacex] * 2
                        board[tempplacey][tempplacex] = 0
                    elif (
                        board[tempplacey][2] == board[tempplacey][tempplacex]
                        and tempplacex > 2
                    ):
                        board[tempplacey][2] = board[tempplacey][tempplacex] * 2
                        board[tempplacey][tempplacex] = 0
                tempplacey = tempplacey - 1
            tempplacex = tempplacex + 1
            tempplacey = 3


    def moveleft(board):
        mergeleft(board)
        tempplacey = 3
        tempplacex = 1
        while tempplacey >= 0 and tempplacex <= 3:
            while tempplacey >= 0:
                if board[tempplacey][tempplacex] > 0:
                    if board[tempplacey][0] == 0:
                        board[tempplacey][0] = board[tempplacey][tempplacex]
                        board[tempplacey][tempplacex] = 0
                    elif board[tempplacey][1] == 0 and tempplacex < 3:
                        board[tempplacey][1] = board[tempplacey][tempplacex]
                        board[tempplacey][tempplacex] = 0
                    elif board[tempplacey][2] == 0 and tempplacex < 2:
                        board[tempplacey][2] = board[tempplacey][tempplacex]
                        board[tempplacey][tempplacex] = 0
                tempplacey = tempplacey - 1
            tempplacex = tempplacex + 1
            tempplacey = 3


    def mergeup(board):
        tempplacey = 3
        tempplacex = 3
        while tempplacex >= 0 and tempplacey >= 0:
            while tempplacex >= 0:
                if board[tempplacey][tempplacex] > 0:
                    if (
                        board[0][tempplacex] == board[tempplacey][tempplacex]
                        and tempplacey > 0
                    ):
                        board[0][tempplacex] = board[tempplacey][tempplacex] * 2
                        board[tempplacey][tempplacex] = 0
                    elif (
                        board[1][tempplacex] == board[tempplacey][tempplacex]
                        and tempplacey > 1
                    ):
                        board[1][tempplacex] = board[tempplacey][tempplacex] * 2
                        board[tempplacey][tempplacex] = 0
                    elif (
                        board[2][tempplacex] == board[tempplacey][tempplacex]
                        and tempplacey > 2
                    ):
                        board[2][tempplacex] = board[tempplacey][tempplacex] * 2
                        board[tempplacey][tempplacex] = 0
                tempplacex = tempplacex - 1
            tempplacey = tempplacey - 1
            tempplacex = 3


    def moveup(board):
        mergeup(board)
        tempplacey = 3
        tempplacex = 3
        while tempplacex >= 0 and tempplacey >= 0:
            while tempplacex >= 0:
                if board[tempplacey][tempplacex] > 0:
                    if board[0][tempplacex] == 0:
                        board[0][tempplacex] = board[tempplacey][tempplacex]
                        board[tempplacey][tempplacex] = 0
                    elif board[1][tempplacex] == 0 and tempplacey > 1:
                        board[1][tempplacex] = board[tempplacey][tempplacex]
                        board[tempplacey][tempplacex] = 0
                    elif board[2][tempplacex] == 0 and tempplacey > 2:
                        board[2][tempplacex] = board[tempplacey][tempplacex]
                        board[tempplacey][tempplacex] = 0
                tempplacex = tempplacex - 1
            tempplacey = tempplacey - 1
            tempplacex = 3


    def mergedown(board):
        tempplacey = 0
        tempplacex = 3
        while tempplacex >= 0 and tempplacey <= 3:
            while tempplacex >= 0:
                if board[tempplacey][tempplacex] > 0:
                    if (
                        board[3][tempplacex] == board[tempplacey][tempplacex]
                        and tempplacey < 3
                    ):
                        board[3][tempplacex] = board[tempplacey][tempplacex] * 2
                        board[tempplacey][tempplacex] = 0
                    elif (
                        board[2][tempplacex] == board[tempplacey][tempplacex]
                        and tempplacey < 2
                    ):
                        board[2][tempplacex] = board[tempplacey][tempplacex] * 2
                        board[tempplacey][tempplacex] = 0
                    elif (
                        board[1][tempplacex] == board[tempplacey][tempplacex]
                        and tempplacey < 1
                    ):
                        board[1][tempplacex] = board[tempplacey][tempplacex] * 2
                        board[tempplacey][tempplacex] = 0
                tempplacex = tempplacex - 1
            tempplacey = tempplacey + 1
            tempplacex = 3


    def movedown(board):
        mergedown(board)
        tempplacey = 0
        tempplacex = 3
        while tempplacex >= 0 and tempplacey <= 3:
            while tempplacex >= 0:
                if board[tempplacey][tempplacex] > 0:
                    if board[3][tempplacex] == 0 and tempplacey < 3:
                        board[3][tempplacex] = board[tempplacey][tempplacex]
                        board[tempplacey][tempplacex] = 0
                    elif board[2][tempplacex] == 0 and tempplacey < 2:
                        board[2][tempplacex] = board[tempplacey][tempplacex]
                        board[tempplacey][tempplacex] = 0
                    elif board[1][tempplacex] == 0 and tempplacey < 1:
                        board[1][tempplacex] = board[tempplacey][tempplacex]
                        board[tempplacey][tempplacex] = 0
                tempplacex = tempplacex - 1
            tempplacey = tempplacey + 1
            tempplacex = 3


    def gameend(board):
        tempplacey = 0
        tempplacex = 0
        x = 100
        while tempplacey < 3:
            while tempplacex < 3:
                if board[tempplacey][tempplacex] < x:
                    x = board[tempplacey][tempplacex]
                tempplacex = tempplacex + 1
            tempplacey = tempplacey + 1
            tempplacex = 0
        if x != 0:
            userpress = x


    while userpress != "x":
        placenewtwo(board)
        boardprint(board)
        userpress = input()
        if userpress == "d":
            moveright(board)
        if userpress == "w":
            moveup(board)
        if userpress == "a":
            moveleft(board)
        if userpress == "s":
            movedown(board)
        gameend(board)
    print("game over, thanks for playing!!")
