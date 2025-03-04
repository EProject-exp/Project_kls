def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


n_terms = int(input("Vendos nje numer: "))
for i in range(n_terms):
    print(fibonacci(i))
