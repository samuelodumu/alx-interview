#!/usr/bin/python3
"""contains `isWinner` function"""


def isWinner(x, nums):
    """determines who the winner of each game is"""
    if not x:
        return None
    if not nums:
        return None
    if x < 1:
        return None
    if len(nums) == 0:
        return None

    def sieve_of_eratosthenes(n):
        # Sieve of Eratosthenes to find all primes up to n
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not primes
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i in range(2, n + 1) if primes[i]]

    maria_wins = 0
    ben_wins = 0

    # Loop through each game
    for n in nums:
        primes = sieve_of_eratosthenes(n)
        num_primes = len(primes)

        # If the number of primes is odd, Maria wins; if even, Ben wins
        if num_primes % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Return the player who won the most rounds, or None if it's a tie
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
