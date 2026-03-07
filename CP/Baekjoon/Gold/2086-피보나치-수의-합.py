MOD = 1000000000

def fibonacci(n):
    if n == 0:
        return (0, 1)

    a, b = fibonacci(n // 2)

    c = (a * ((2 * b - a) % MOD)) % MOD
    d = (a * a + b * b) % MOD

    if n % 2 == 0:
        return (c, d)
    else:
        return (d, (c + d) % MOD)


a, b = map(int, input().split())

fib_b = fibonacci(b + 2)[0]
fib_a = fibonacci(a + 1)[0]

print((fib_b - fib_a) % MOD)