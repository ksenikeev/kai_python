import cProfile


def public_key():
    a = 3
    b = 7
    return [a, b]

def private_key():
    return 1

def my_pow(m,n, d):
    return pow(m,n,d)

if (__name__ == '__main__'):
    d = 1
    while ((d * 5) % 12 != 1):
        d = d + 1
    print(d)