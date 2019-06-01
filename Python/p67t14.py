a = int(input("Введите натуральное число: "))

maxdig = 0
while a != 0:
	dig = a % 10
	if dig > maxdig: maxdig = dig

	a = a // 10

print("Наибольшая цифра дяситичной записи: ",maxdig)