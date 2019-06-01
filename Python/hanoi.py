def Hanoi(n, k, m):
	if n <= 0: return
	p = 6 - k - m
	Hanoi( n-1, k, p)
	print( k, "->", m )
	Hanoi( n-1, p, m )

n = int(input("Введите количество дисков: "))

Hanoi(n, 1, 3)