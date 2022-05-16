#программа демонстрирует алгоритм RSA

private_key = None #Закрытый ключ
public_key = None  #Открытый ключ
m=453 #сообщение для шифровки
m_1=None #расшифрованное сообщение
с=None   #сообщение в зашифрованном виде

#Генерация ключей
def make_keys(p, q):

    #Проверить на простоту p и q

    global public_key  #будем работать с инициализацией глобальных переменных
    global private_key #

    n = p * q
    print(f'n={n}')
    phi = (p - 1) * (q - 1)
    print(f'phi={phi}')
    # подбираем e взаимно простым с phi
    e = 3
    while (phi % e == 0):
        e = e + 1
    print(f'e={e}')
    public_key = [e, n]
    print(f'public_key={public_key}')

    # подбираем d как одно из решений уравнения d*e ≡ 1 (mod phi)
    d = 1
    while ((d * e) % phi != 1):
        d = d + 1

    private_key = [d, n]
    print(f'private_key={private_key}')

    return

# операция возведения в степень по модулю
# a^b mod v
# в примере используется стандартная функция
# необходимо реализовать свой вариант
def my_pow(a,b, v):
    return pow(a, b, v)

if (__name__ == '__main__'):
    make_keys(13,37) # генерируем ключи
    c = my_pow(m, public_key[0], public_key[1])  #шифруем сообщение m с помощью открытого ключа
    print(f'c={c}')
    m_1 = my_pow(c, private_key[0], private_key[1]) # расшифровываем сообщение c с помощью закрытого ключа
    print(f'm={m}, m\'={m_1}')