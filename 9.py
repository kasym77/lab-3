from random import randint

n = randint(1,100)
k = input("Угадайте целое число от 1 до 100: ")

while 1:
  if k == "Выход":
    print("В следующий раз повезёт!")
    break

  k = int(k)

  if k == n:
    print("Вы угадали")
    break

  print("Ваше число " + ("больше" if k > n else "меньше") + ", чем задумал компьютер")

  k = input("Повторите попытку: ")

print("Загаданным числом было: " + str(n))
