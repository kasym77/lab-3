import random

# число попыток угадать
guesses_made = 0

# получаем имя пользователя из консольного ввода
name = input('Hello! What is your name?\n')

# получаем случайное число в диапазоне от 1 до 30
number = random.randint(1, 30)
print ('Great, {0}, I guessed a number between 1 and 30. '.format(name))

# пока пользователь не превысил число разрешенных попыток - 6
while guesses_made < 6:
   
    # получаем число от пользователя
    guess = int(input('Write a number: '))
   
    # увеличиваем счетчик числа попыток
    guesses_made += 1

    if guess < number:
        print ('Your number is less than what I wished for')

    if guess > number:
        print ('Your number is greater than what I guessed')

    if guess == number:
        break

if guess == number:
    print ('Wow, {0}! You guessed my number using {1} hazards!'.format(name, guesses_made))
else:
    print ('But I didn’t guess right! I wished for the number {0}'.format(number))
   
