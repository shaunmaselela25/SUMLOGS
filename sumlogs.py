"""
A program that computes the sum of the logarithms of all the primes from 2 to some 
number n, and prints:
  - the sum of the logs of the primes,
  - the number n,
  - the ratio of these two quantities.

According to the Prime Number Theorem, this ratio approaches 1 as n increases, 
though not monotonically.
"""
import math


def is_prime(num: int) -> bool:
    """Return True if num is prime, else False."""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def sum_of_logs_of_primes(n: int) -> float:
    """Return the sum of logarithms of all primes from 2 up to n (inclusive)."""
    return sum(math.log(i) for i in range(2, n + 1) if is_prime(i))


def main():
    n_values = [10, 100, 1000, 10000, 100000]
    for n in n_values:
        sum_logs = sum_of_logs_of_primes(n)
        ratio = sum_logs / n
        print(f"n = {n:6d}, Sum(log primes) = {sum_logs:.6f}, Ratio = {ratio:.6f}")


if __name__ == "__main__":
    main()
