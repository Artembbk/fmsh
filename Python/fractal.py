from graph import *

def square(x, y, a):
	rectangle( x, y, x+a, y+a)

def fractal(x, y, a, level, pos):
	if level < 1: return

	square(x, y, a)
	newa = a//2
	
	if (pos == 0) or (pos == 2) or (pos == 3) or (pos == 4): fractal( x + a, y + a, newa, level - 1, 3 )
	if (pos == 0) or (pos == 1) or (pos == 3) or (pos == 4): fractal( x - newa, y + a, newa, level - 1, 4 )
	if (pos == 0) or (pos == 1) or (pos == 2) or (pos == 4): fractal( x - newa, y - newa, newa, level - 1, 1 )
	if (pos == 0) or (pos == 1) or (pos == 2) or (pos == 3): fractal( x + a, y - newa, newa , level - 1, 2 )

x,y = map( int, input("Введите координаты верхнего левого угла основного квадрата через пробел: ").split() )
a = int(input("Введите длину стороны основного квадрата: "))
level = int(input("Введите уровень фрактала: "))

penColor("black")
fractal(x, y, a, level, 0)

run()