from typing import Final

from prime_factors import PrimeFactors


class TestPrimeFactors:
    CASES: Final[dict[int, list[int]]] = {
        1: [],
        2: [2],
        4: [2, 2],
        4: [2, 2],
        8: [2, 2, 2],
        9: [3, 3],
    }

    def test_prime_factors(self) -> None:
        for number, expected_factors in self.CASES.items():
            assert PrimeFactors.calculate(number) == expected_factors
