def is_correct_word(word):
	for goal_word in goal_words:
		if word in goal_word: return True
	return False

def is_goal(word):
	for goal_word in goal_words:
		if word == goal_word: return True
	return False

N = int(input("Введите количесвто слов для игры: "))
print("Введите слова для игры через Enter:")
goal_words = [ input() for i in range(N) ]

word = ""
while True:
	print("Слова-цели: ", *goal_words)
	print("Текущее слово: ", word)
	
	if is_goal(word): break
	
	letter = input("Введите букву, которую вы хотите добавить к текущему слову: ")

	if len(letter) > 1: 
		print("Ошибка! Необходимо ввести лишь одну букву. Повторите ход.")
		continue
	if is_correct_word(word + letter): 
		word = word + letter
	else: 
		print("Ошибка! Полученное слово не является началом ни одного слова-цели. Повторите ход.")
		continue

print("Игра закончилась!")