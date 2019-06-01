from graph import *

FIELD_S = 300
SQUARE_S = 100
X_FIELD = 100
Y_FIELD = 100

move = 0
squares = [ [0]*3 for i in range(3) ]

def square(x, y, a):
	return rectangle( x, y, x+a, y+a)

def cross(x, y, a):
    line(x, y, x+a, y+a)
    line(x+a, y, x, y+a)

def init():
    penColor("black")
    for i in range(3):
        for j in range(3):
            squares[i][j] = square(X_FIELD + SQUARE_S*j, Y_FIELD + SQUARE_S*i, SQUARE_S)

def hit(x, y, obj):
    x1, y1, x2, y2 = coords(obj)
    return (x1 <= x <= x2) and (y1 <= y <= y2)

def check():
    A = [ [0]*3 for i in range(8) ]
    for i in range(3):
        A[6][i] = squares[i][i]
        A[7][i] = squares[i][2-i]
        for j in range(3):
            A[i][j] = squares[i][j]
            A[j+3][i] = squares[i][j]
    for L in A:
        if L[0] == L[1] == L[2]: return True

def finish_game(w):
    if w == 1:
        label("Победили крестики!", 100, 60)
    elif w == 0:
        label("Победили нолики!", 100, 60)
    else:
        label("Ничья!", 100, 60)

    for i in range(3):
        for j in range(3):
            if type(squares[i][j]) == int: squares[i][j] = "W"

def mouseClick(event):
    global move
    for i in range(3):
        for j in range(3):
            if type(squares[i][j]) == int:
                if hit(event.x, event.y, squares[i][j]):
                    move += 1
                    x1, y1, x2, y2 = coords(squares[i][j])
                    if move % 2 == 1:
                        cross(x1, y1, SQUARE_S)
                        squares[i][j] = "X"
                    else:
                        circle( x1 + SQUARE_S//2, y1 + SQUARE_S//2, SQUARE_S//2 )
                        squares[i][j] = "O"

    if check() and move % 2 == 1:
        finish_game(1)
    elif check() and move % 2 == 0:
        finish_game(0)
    elif move == 9:
        finish_game(2)



init()
onMouseClick( mouseClick )
run()
