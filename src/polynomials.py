from collections.abc import Callable


def define_polynomial(coefs: list[float]) -> Callable:
    def p(x: float) -> float:
        result = 0
        index = range(len(coefs))
        result = [a * x ** i for a, i in zip(coefs, index, strict=False)]

        return sum(result)

    return p

def test_polynomial(coefs: list[float], x: float, result: float) -> None:
    p = define_polynomial(coefs)

    if p(x) != result:
        msg = "Expected to be equal."
        raise ValueError(msg)

def test_polynomial_with_error(
    coefs: list[float],
    x: float,
    result: float,
    error: float,
) -> None:
    p = define_polynomial(coefs)

    if abs(p(x) - result) > error:
        msg = "Expected to be less than the error."
        raise ValueError(msg)
