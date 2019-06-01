def summarize(list):
	sum = 0
	for elem in list:
		sum += int(elem)
	return sum


str = input("Введите сумму и разность натрульных чисел: ")

addends = str.split('+')

for i in range(len(addends)):
	if "-" in addends[i]:
		dif = addends[i].split("-")
		addends[i] = dif[0] - summarize(dif[1:])

sum = summarize(addends)
print(sum)
