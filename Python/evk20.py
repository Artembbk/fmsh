a, b = map(int, input("Введите два натуральных числа через пробел: ").split())

i=0
while a!=0 and b!=0:
	i=+1
	if a > b:
		a = a % b
	else:
		b = b % a

print("НОД чисел a и b равен: ",a+b)
print("Количество шагов: ",i)