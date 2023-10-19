n = int(input())
 
factorial = 1 #Мы создаём переменную с именем "factorial" и устанавливаем её равной 1.
while n > 1:
    factorial *= n #Здесь мы умножаем значение "factorial" на значение "n" и сохраняем результат обратно в "factorial"
    n -= 1
 
print(factorial)
