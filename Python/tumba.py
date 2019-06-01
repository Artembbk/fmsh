k = int(input("Введите длину слов: "))

alphabet = {"Ы", "Ш", "Ч", "Э"}
vowels = {"Ы", "Э"}
def allWords(word, alphabet, k):
	if k < 1:
		for c in word:
			if c in vowels: 
				print(word)
				break
		return
	for c in alphabet:
		if len(word) != 0 and (c in vowels and word[-1] in vowels): continue
		allWords(word + c, alphabet, k-1)

allWords("", alphabet, k)