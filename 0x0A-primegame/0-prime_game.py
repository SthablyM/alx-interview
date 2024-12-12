#!/usr/bin/python3
"""
prime game
"""


def isWinner(x, nums):
    def sieve(max_n):
        """
        Generate a list of primes up to
        max_n using the Sieve of Eratosthenes.
        """
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_n + 1, i):
                    is_prime[j] = False
        return is_prime

    def count_primes(n, primes):
        """Count how many primes are <= n."""
        return sum(primes[:n + 1])

    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes(n, primes)
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
