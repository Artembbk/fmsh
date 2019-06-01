from graph import *

def update():
    global x1, x2, dx1, dx2

    x1 += 5
    x2 -= 5
    moveObjectBy(obj1, dx1, 0)
    moveObjectBy(obj2, dx2, 0)

    if (x1 + 30) == 150: dx1 = -dx1
    if x2 == 350: dx2 = -dx2


brushColor("blue")
penColor("black")
rectangle(150,150,350,300)

x1 = 10
y1 = 200
dx1 = 5

x2 = 460
y2 = 200
dx2 = -5

penColor("black")
brushColor("green")
obj1 = rectangle(x1, y1, x1+30, y1+30)
obj2 = rectangle(x2, y2, x2+30, y2+30)

onTimer(update, 50)

run()
