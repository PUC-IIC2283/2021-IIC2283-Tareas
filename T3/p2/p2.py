import math

def phi(n):
    ans = n
    i = 2
    while i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            ans -= ans // i
        i += 1
    if n > 1: ans -= ans // n
    return ans

def sieve(n):
    isprime = [True] * (n+1)
    limit = math.floor(math.sqrt(n))
    for x in range(2, limit+1):
        if isprime[x]:
            for y in range(x*x, n+1, x):
                isprime[y] = False                
    primes = []
    for x in range(2, n+1):
        if isprime[x]: primes.append(x)
    return primes

def factorial_prime_factorization(x, sign):
    for p in primes:
        if p > x: break
        e = 0
        tmp = x
        while True:
            tmp //= p
            if tmp <= 0: break
            e += tmp
        exps[p] += sign * e

def binary_exp(a, b, m):
    a %= m
    res = 1
    while b > 0:
        if (b&1): res = (res * a) % m
        a = (a * a) % m
        b >>= 1
    return res

if __name__ == '__main__':
    n, k = map(int, input().split())    
    x = phi(n)
    primes = sieve(x)
    exps = [0] * (x+1)
    if k > x:
        print('-1')
    else:
        factorial_prime_factorization(x, 1)
        factorial_prime_factorization(k, -1)
        factorial_prime_factorization(x-k, -1)
        n_zeroes = min(exps[2], exps[5])
        exps[2] -= n_zeroes
        exps[5] -= n_zeroes
        res = 1
        for p in primes:
            if p > x: break
            res = (res * binary_exp(p, exps[p], 10)) % 10
        print(res)