#!/usr/bin/python3
""" Prime Game"""


def isWinner(x, nums):
    """
    Determine the winner of each round and the overall winner.

    :param x: Number of rounds (integer)
    :param nums: List of integers representing the range [1, n] for each round
    :return: Name of the player that won the most rounds ('Maria' or 'Ben'),
     or None if it's a tie
    """
    def sieve_of_eratosthenes(max_n):
        """
        Generate a list indicating whether numbers up to max_n are prime.
        """
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(max_n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_n + 1, i):
                    is_prime[j] = False

        return is_prime

    def count_primes_up_to(n, prime_flags):
        """Count the number of primes up to n."""
        return sum(prime_flags[:n + 1])

    if x < 1 or not nums:
        return None

    max_n = max(nums)
    prime_flags = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes_up_to(n, prime_flags)

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
