# объявление функции

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def is_valid_password(password):
    pass_l = password.split(':')
    if len(pass_l) == 3:
        return pass_l[0] == pass_l[0][-1::-1] and is_prime(int(pass_l[1])) and int(pass_l[2]) % 2 == 0
    return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
