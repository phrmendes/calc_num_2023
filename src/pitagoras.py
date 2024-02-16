def pitagoras(t: tuple[int, int, int]) -> bool:
    if t[0]**2 + t[1]**2 == t[2]**2:
        return True
    return False

def test_pitagoras(tests: dict[tuple, bool]) -> None:
    for key, value in tests.items():
        result = pitagoras(key)

        if result != value:
            msg = "Expected to be true."
            raise ValueError(msg)
