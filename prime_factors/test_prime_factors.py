from collections import namedtuple
from typing import Final

from prime_factors import PrimeFactors


class TestPrimeFactors:
    Case = namedtuple('TestCase', ('number', 'factors'))

    CASES: Final[tuple[Case, ...]] = (
        Case(1, []),
        Case(2, [2]),
        Case(4, [2, 2]),
        Case(4, [2, 2]),
        Case(8, [2, 2, 2]),
        Case(9, [3, 3]),
    )

    def test_prime_factors(self) -> None:
        for test_case in self.CASES:
            factors = PrimeFactors.calculate(test_case.number)
            assert factors == test_case.factors
