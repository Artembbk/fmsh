while True:
	full_name = input("Введите Ф.И.О через пробел: ")

	full_name = full_name.strip().split()
	if len(full_name) != 3: 
		print("Ошибка! Необходимо ввести 3 слова!")
		continue
	else:
		for i in range(len(full_name)):
			full_name[i] = full_name[i][0].upper() + full_name[i][1:]
		
		print( full_name[1][0] + "." + full_name[2][0] + ". " + full_name[0], sep="")

	break