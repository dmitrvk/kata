class PrimeFactors:
    @staticmethod
    def calculate(number: int) -> list[int]:
        factors: list[int] = []
        divisor: int = 2

        while number > 1:
            while number % divisor == 0:
                factors.append(divisor)
                number //= divisor

            divisor += 1

        return factors
