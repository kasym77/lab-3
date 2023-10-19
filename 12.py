def isitgood(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

try:
    N = int(input("Введите положительное целое число N: "))
    if N < 2:
        print("В указанном диапазоне нет простых чисел.")
    else:
        print("Простые числа от 1 до", N, "это:")
        num = 2
        while num <= N:
            if is_prime(num):
                print(num, end=" ")
            num += 1
except ValueError:
    print("Неверный ввод. Пожалуйста, введите положительное целое число.")
