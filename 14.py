def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num

while True:
    user_input = int(input("Введите число для проверки на простоту (или -1 для выхода): "))
    if user_input == -1:
        break

    if is_prime(user_input):
        print(f"{user_input} - простое число.")
    else:
        next_prime = find_next_prime(user_input)
        print(f"{user_input} не является простым. Следующее простое число: {next_prime}")
