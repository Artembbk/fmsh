n = int(input("Введите натуральное число: "))

k = 2
while k < n:
	if n % k == 0: break
	k += 1

if k == n:
	print(n,"-простое число")
else:
	print(n,"не простое число")
	