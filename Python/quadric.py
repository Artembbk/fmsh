from math import sqrt

a, b, c = map(int, input("Введите коэфиценты квадратного уравнения через пробел: ").split())

if a != 0:
	d = b**2 - 4*a*c
	
	if d > 0:
		x1 = ( -b-sqrt(d) )/2*a
		x2 = ( -b+sqrt(d) )/2*a
		print("x1 = {}; x2 = {}".format(x1, x2))
	
	elif d == 0:
		x = -b/2*a
		print("x1 = x2 = {}".format(x))
	
	else:
		print("Данное уравнение не имеет действительных решений")

else:
	if b!=0:
		x = -c/b
		print("x ={}".format(x))
	else:
		if c==0:
			print("Данное уравнение имеет бесконечное колчество решиний")
		else:
			print("Данное уравнение не имеет решений")