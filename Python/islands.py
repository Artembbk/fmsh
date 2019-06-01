def printMatrix(A):
    for row in A:
        for x in row:
            print("{:3}".format(x), end="")
        print()

def find_island():
    for i in range(b):
        for j in range(a):
            if M[i][j] == "1": return i, j
    else: return -1, -1

def explore_island(i, j, passed):
    if M[i][j] != "2":
        M[i][j] = "2"
        passed.append([i, j])

    if (i - 1 > 0) and ( M[i - 1][j] == "1"):
        explore_island(i - 1, j, passed)
    elif (j - 1 > 0) and ( M[i][j - 1] == "1"):
        explore_island(i, j-1, passed)
    elif (i + 1 < b) and ( M[i + 1][j] == "1"):
        explore_island(i + 1, j, passed)
    elif (j + 1 < a) and ( M[i][j + 1] == "1"):
        explore_island(i, j + 1, passed)
    else:
        passed.remove([i, j])
        if len(passed) > 0:
            explore_island(passed[0][0], passed[0][1], passed)
        else:
            return

amount = 0

a, b = map(int, input("Введите размерность карты через пробел: ").split())
M = [ ["X"]*a for i in range(b) ]
printMatrix(M)

for i in range(b):
    for j in range(a):
        M[i][j] = input("Введите значение клетки: ")
        printMatrix(M)
while True:
    i, j = find_island()
    if i == -1: break
    explore_island(i, j, [])
    amount += 1

print("Количество островов:", amount)
