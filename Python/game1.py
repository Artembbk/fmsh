word = input("Введите слово для игры: ")

while len(word) > 0:
	print("Ввыберите действие:")
	print("1. Стереть одну букву")
	print("2. Стереть все одинаковые буквы")
	move = int(input())
	

	if move == 1:
		letter_ind = int(input("Введите неотрицателтный индекс буквы, начиная с нуля: "))
		if (letter_ind > len(word) - 1) or (letter_ind < 0): 
			print("Ошибка! Индекс первышает длину слова или меньше нуля. Повторите ход.")
			continue
		
		word = word[:letter_ind] + word[letter_ind + 1:]
	
	elif move == 2:
		letter = input("Введите букву: ")
		
		if letter in word:
			while letter in word:
				letter_ind = word.find(letter)
				word = word[:letter_ind] + word[letter_ind + 1:]
		else: 
			print("Ошибка! Буква отсутствует в слове. Повторите ход.")
	
	else: 
		print("Ошибка! Такого действия нет. Повторите ход.")

	print(word)

print("Игра закончилась!")
		

