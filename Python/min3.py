from random import randint

N = int(input("Введите длину массива: "))
if input("Введите 'r', если хотите заполнить массив случайно и 'Enter', если самостоятельно: ") == "r":
	A = [ randint(0, 999) for x in range(N) ]
else:
	A = [ int(input()) for x in range(N) ]

for i in range(3):
	minim = min(A)
	print("Минимум-{}: {}".format(i+1, minim))
	
	while minim in A:
		minim_in = A.index(minim)
		A = A[:minim_in] + A[minim_in + 1:]
