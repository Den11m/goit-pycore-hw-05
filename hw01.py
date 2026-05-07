

def caching_fibonacci():
    """Функція, що створює замикання з кешем для обчислення чисел Фібоначчі."""
    cache = {}

    def fibonacci(n):
        """Обчислює n-е число Фібоначчі з використанням кешування."""
        # Базові випадки
        if n <= 0: return 0
        if n == 1: return 1
        
        # Перевірка кешу
        if n in cache: return cache[n]

        # Рекурсивне обчислення та збереження в кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
