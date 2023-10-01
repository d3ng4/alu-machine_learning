#!/usr/bin/env python3


class Binomial:
    def __init__(self, data=None, n=1, p=0.5):
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if not (0 < p < 1):
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.n, self.p = self.calculate_parameters(data)

    def calculate_parameters(self, data):
        p = sum(data) / len(data)
        n = round(p * (1 - p) / (p * p))
        p = sum(data) / (n * len(data))
        return int(n), float(p)

    def pmf(self, k):
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        coeff = self._bin_coeff(self.n, k)
        pmf_value = coeff * (self.p ** k) * ((1 - self.p) ** (self.n - k))
        return pmf_value

    def cdf(self, k):
        k = int(k)
        if k < 0:
            return 0
        cdf_value = 0
        for i in range(k + 1):
            cdf_value += self.pmf(i)
        return cdf_value

    def _bin_coeff(self, n, k):
        numerator = self._factorial(n)
        denominator = self._factorial(k) * self._factorial(n - k)
        coeff = numerator / denominator
        return coeff

    def _factorial(self, n):
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial
