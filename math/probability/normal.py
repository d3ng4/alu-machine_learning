#!/usr/bin/env python3


class Normal:
    def __init__(self, data=None, mean=0., stddev=1.):
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean, self.stddev = self.calculate_mean_stddev(data)

    def calculate_mean_stddev(self, data):
        n = len(data)
        mean = sum(data) / n
        stddev = (sum((x - mean) ** 2 for x in data) / n) ** 0.5
        return float(mean), float(stddev)

    def z_score(self, x):
        z = (x - self.mean) / self.stddev
        return z

    def x_value(self, z):
        x = z * self.stddev + self.mean
        return x
