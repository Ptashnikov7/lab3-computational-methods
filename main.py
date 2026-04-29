# Модель: Метод Ньютона (5 семестр)
# Автор: Пташников Василь AI-235.

def f(x):
    return x**2 - 2

def f_prime(x):
    return 2*x

def newton_method(x0, eps=0.0001):
    x = x0
    while abs(f(x)) > eps:
        x = x - f(x)/f_prime(x)
    return x

root = newton_method(1)
print("Корінь:", root)
