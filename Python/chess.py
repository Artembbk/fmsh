a = int(input("Введите размер доски: "))
F = [ [0]*a for i in range(a) ]
F[a//2][a//2] = 1

def count_moves(x,y):
    p_moves = [[x-1, y-2], [x+1, y-2], [x+2, y-1], [x+2, y+1], [x+1, y+2], [x-1, y+2], [x-2, y+1], [x-2, y-1]]
    while True:
        for move in p_moves:
            if not((0 <= move[0] <= 4) and (0 <= move[1] <= 4) and (F[move[1]][move[0]] == 0)):
                p_moves.remove(move)
                break
        else: break
    return len(p_moves)

def make_move(x, y):
    p_moves = [[x-1, y-2], [x+1, y-2], [x+2, y-1], [x+2, y+1], [x+1, y+2], [x-1, y+2], [x-2, y+1], [x-2, y-1]]
    while True:
        for move in p_moves:
            if not((0 <= move[0] <= 4) and (0 <= move[1] <= 4) and (F[move[1]][move[0]] == 0)):
                p_moves.remove(move)
                break
        else: break

    moves_amount = []
    for move in p_moves:
        moves_amount.append(count_moves(move[0], move[1]))

    next_move_ind = moves_amount.index(min(moves_amount))
    F[p_moves[next_move_ind][1]][p_moves[next_move_ind][0]] = 1
    print("MOVE: ", "(", p_moves[next_move_ind][0] + 1, ":", p_moves[next_move_ind][1] + 1, ")", sep = "" )

    if check(): return

    make_move(p_moves[next_move_ind][0], p_moves[next_move_ind][1])

def check():
    sum = 0
    for i in range(a):
        for j in range(a):
            sum += F[i][j]
    if sum == a*a: return True

print("START POSITION: ", "(", a//2 + 1, "; ", a//2 + 1, ")", sep="")
make_move(a//2,a//2)
