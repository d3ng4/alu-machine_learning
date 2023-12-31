#!/usr/bin/env python3


class Exponential:
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
        return float(len(data)) / total

    def pdf(self, x):
        if x < 0:
            return 0
        else:
            # Calculate the PDF using the exponential distribution formula
            pdf_value = self.lambtha * (2.71828 ** (-self.lambtha * x))
            return pdf_value

    def cdf(self, x):
        if x < 0:
            return 0
        else:
            # Calculate the CDF using the exponential distribution formula
            cdf_value = 1 - (2.71828 ** (-self.lambtha * x))
            return cdf_value
