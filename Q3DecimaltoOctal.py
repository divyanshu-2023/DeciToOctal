def decimal_to_octal(decimal_num):
    return oct(decimal_num).replace("0o", "")

def reverse_integer(num):
    return int(str(num)[::-1])

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci_recursive(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

def nth_fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

print(decimal_to_octal(25))
print(reverse_integer(12345))
print(fibonacci_recursive(7))
print(nth_fibonacci(6))
