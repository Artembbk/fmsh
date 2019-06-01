summ = 0
i = 0
while True:
	n = int(input())
	if n == 0: break
	i = i + 1
	summ = summ + n

print("Среднее арифметическое: ",summ/i)