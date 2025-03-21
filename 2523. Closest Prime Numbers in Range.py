class Solution(object):
    def closestPrimes(self, left, right):
        l = right - left + 1
        arr = is_prime(left, right)

        if len(arr) < 2:
            return [-1, -1]
        
        mini = -1
        minl = l
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] < minl:
                minl = arr[i + 1] - arr[i]
                mini = arr[i]
        return [mini, mini + minl]


def is_prime(start, num):
    out = list()
    sieve = [True] * (num + 1)
    for p in range(2, num + 1):
        if (sieve[p]):
            if p >= start:
                out.append(p)
            for i in range(p, num + 1, p):
                sieve[i] = False
    return out


class BestSolution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(right ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, right + 1, i):
                    sieve[j] = False
        
        primes = [i for i in range(left, right + 1) if sieve[i]]
        
        if len(primes) < 2:
            return [-1, -1]
        
        min_gap = float('inf')
        result = [-1, -1]
        
        for i in range(1, len(primes)):
            gap = primes[i] - primes[i-1]
            if gap < min_gap:
                min_gap = gap
                result = [primes[i-1], primes[i]]
        
        return result


print(Solution().closestPrimes(19, 31))
print(BestSolution().closestPrimes(19, 31))
