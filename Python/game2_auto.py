N = int(input("Введите количесвто слов для игры: "))
print("Введите слова для игры через Enter:")
goal_words = [ input() for i in range(N) ]

odd_goal_words = [ x for x in goal_words if len(x) % 2 != 0 ]
even_goal_words = [ x for x in goal_words if len(x) % 2 == 0 ]

for odd_word in odd_goal_words:
	for i in range(len(odd_word)):
		for even_word in even_goal_words:
			if odd_word[:i] in even_word:
