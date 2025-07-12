board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
def is_vacumn(row, column):
    if (board[row-1][column - 1] == " "):
        return True
    print(f"({row}, {column} is already marked)")
    return False
def is_valid(row, column):
    if (1 <= row <= len(board) and 1<= column <= len(board[0])):
        return True
    print("Out of range")
    return False
def check(row, column):
    if ( is_valid(row, column) and is_vacumn(row, column)):
        return True
    return False
def draw_board():
    print("_______")
    for i in range(len(board)):
        print("|", end="")
        for j in range(len(board[1])):
            print(board[i][j], end="")
            print("|",end="")
        print()
        print("-------")
def is_win():
    #check rows
    for i in range(len(board)):
        if all(board[i][j] == "X" for j in range(len(board[0]))): 
            return 1
        elif all(board[i][j] == "Y" for j in range(len(board[0]))):
            return 2
    #check columns
    for i in range(len(board[0])):
        if all(board[j][i] == "X" for j in range(len(board))):
            return 1
        elif all(board[j][i] == "Y" for j in range(len(board))):
            return 2
    if all(board[i][i] == "X" for i in range(len(board))):
        return 1
    elif all(board[i][i] == "Y" for i in range(len(board))):
        return 2
    elif (is_draw()):
        print("Draw")
        return 0
        
def is_draw():
    for row in board:
        if " " in row:
            return False
    return True
    

def main():
#ask user for ticking
    while True:
        draw_board()
        #ask for x's choice
        while True:
            rx = int(input("X's choice (row): "))
            cx = int(input("X's choice (column): "))
            if (check(rx, cx)):
                break
        #mark X
        board[rx - 1][cx - 1] = "X"
        draw_board()
        result = is_win()
        if (result == 1):
            print("X win")
            break
        elif (result == 0):
            print("Draw")
            break
        #ask for Y's choice
        while True:
            ry = int(input("Y's choice (row): "))
            cy = int(input("Y's choice (column): "))
            if (check(ry, cy)):
                break
        #Mark Y
        board[ry - 1][cy - 1] = "Y"
        result = is_win()
        if (result == 2):
            print("Y's win")
            break
        elif (result == 0):
            print("Draw")
            break
        

if __name__ == "__main__":
    main()
    
    