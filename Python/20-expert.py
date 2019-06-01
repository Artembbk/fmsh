otvet = input("Кормит детей молоком? ")
if otvet == "да":
  print("Млекопитающее.")
  otvet = input("Ест мясо? ")
  if otvet == "да":
    print("Хищник.")
  else:
    print("Не знаю.")
else:
  otvet = input("Имеет перья? ")
  if otvet == "да":
    print("Птица.")
  else:
    print("Не знаю.")
