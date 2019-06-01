from random import randint

def number_sum(n):
	sum = 0
	while n > 0:
		sum = sum + n%10
		n = n//10
	return sum

N = int(input("Введите длину массива: "))
A = [ randint(100, 999) for x in range(N) ]

nMax = 0
for i in range(1, N):
	if number_sum(A[i]) > number_sum(A[nMax]):
		nMax = i

print("Элемент с наибольшой суммой цифр:", A[nMax], "Индекс:", nMax)
