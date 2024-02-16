def fibonacci(n: int) -> int:
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

def n_first_fibonacci(n: int) -> list[int]:
    return [fibonacci(i) for i in range(n)]
