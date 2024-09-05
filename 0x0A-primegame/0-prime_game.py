#!/usr/bin/python3
'''prime_game module''


def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    primes = [i for i in range(2, n + 1) if sieve[i]]
    return primes

def isWinner(x, nums):
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    def play_game(n):
        prime_set = set(range(1, n + 1))
        turn = 0  # 0 for Maria, 1 for Ben
        
        for prime in primes:
            if prime > n:
                break
            if prime in prime_set:
                turn = 1 - turn  # Switch turns
                multiples = set(range(prime, n + 1, prime))
                prime_set -= multiples
        
        return 'Ben' if turn == 1 else 'Maria'
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = play_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
