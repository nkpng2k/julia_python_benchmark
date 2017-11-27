import numpy as np
from timeit import timeit


class TimeFunctions(object):

    def __init__(self, fib_num=None, func_coeffs=None):
        self.fib_num = fib_num
        self.coeffs = func_coeffs

    def f(self, x):
        return x**2 - 2

    def f_prime(self, x):
        return 2*x

    def recursive_roots(self):
        initial_conditions = np.arange(-100, 100, 0.01)
        roots = np.zeros_like(initial_conditions)

        for j, x_0 in enumerate(initial_conditions):
            x = x_0
            for i in xrange(1, 1000):
                x = x - (self.f(x) / self.f_prime(x))

            roots[j] = x

        return roots

    def numpy_roots(self):
        coeffs = self.func_coeffs
        return np.roots(coeffs)

    def rec_fib(self):
        if self.fib_num > 1:
            return self.rec_fib(self.fib_num-2) + self.rec_fib(self.fib_num-1)
        return self.fib_num

    def iterative_fibonacci(self):
        var1 = 0
        var2 = 1
        if self.fib_num < 2:
            return self.fib_num
        for i in xrange(1, self.fib_num - 1):
            fib_num = var1 + var2
            var1 = var2
            var2 = fib_num
        return fib_num

    def time_function(self, function, num_iter=1):
        print timeit(function, num_iter)


if __name__ == "__main__":
    timed = TimeFunctions(100, [1, 0, -2])
    print timeit(timed.recursive_roots, number=10)
    print timeit(timed.numpy_roots, number=10)
    print timeit(timed.rec_fib, number=10)
    print timeit(timed.iterative_fibonacci, number=10)


"""
bottom of page
"""
