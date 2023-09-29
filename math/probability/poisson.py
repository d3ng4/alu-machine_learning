#!/usr/bin/env python3


class Poisson:
    def __init__(self, data=None, lambtha=1.):
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = self.calculate_lambtha(data)

    def calculate_lambtha(self, data):
        total = sum(data)
        return float(total) / len(data)

    def pmf(self, k):
        k = int(k)
        if k < 0:
            return 0
        else:
            # Calculate the PMF using the Poisson distribution formula
            pmf_value = (self.lambtha ** k) * (2.71828 **
                                               (-self.lambtha)) / self.factorial(k)
            return pmf_value

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)
