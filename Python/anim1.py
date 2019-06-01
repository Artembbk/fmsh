from graph import *

def update():
    global x1, x2
    x1 += 5
    x2 -= 5
    moveObjectBy(obj1, 5, 0)
    moveObjectBy(obj2, -5, 0)

brushColor("blue")
penColor("black")
rectangle(150,150,350,300)

x1 = 10
y1 = 200
x2 = 450
y2 = 200
penColor("black")
brushColor("green")
obj1 = rectangle(x1, y1, x1+30, y1+30)
obj2 = rectangle(x2, y2, x2+30, y2+30)

onTimer(update, 50)

run()
