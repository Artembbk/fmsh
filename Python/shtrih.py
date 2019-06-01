from graph import *

x1,y1 = map(int, input("Введите координаты первой вершины через пробел: ").split())
x2,y2 = map(int, input("Введите координаты первой вершины через пробел: ").split())
x3,y3 = map(int, input("Введите координаты первой вершины через пробел: ").split())
n = int(input("Введите количество линий: "))

penColor("black")
polygon([(x1,y1),(x2,y2),(x3,y3),(x1,y1)])

if x1 >= x2 or x1 >= x3:
	if x2 <= x3: x1, y1, x2, y2 = x2, y2, x1, y1
	else: x1, y1, x3, y3 = x3, y3, x1, y1

if x1 == x2: x2, y2, x3, y3 = x3, y3, x2, y2


hx = (x2-x1) / n
hy = (y3-y1) / n
xa = x1 + hx
yb = y1 + hy
while xa < x2:
	ya = ( (xa - x1)*(y2 - y1)/(x2 - x1) ) + y1
	xb = ( (yb - y1)*(x3 - x1)/(y3 - y1) ) + x1

	line( round(xa), round(ya), round(xb), round(yb))
	xa = xa + hx
	yb = yb + hy

print(x1,y1,x2,y2,x3,y3)
run()