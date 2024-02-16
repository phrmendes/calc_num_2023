def collatz(n: int) -> int:
    if n == 0:
        return 0

    i = 1

    while True:
        n = n // 2 if n % 2 == 0 else 3 * n + 1

        if n == 1:
            return i

        i += 1

def test_collatz(tests: list[tuple[int, int]]) -> None:
    for a, b in tests:
        result = collatz(a)

        if result != b:
            msg = "Expected to be equal."
            raise ValueError(msg)
