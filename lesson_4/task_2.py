from timeit import timeit


def prime(n):
    counter = 1
    current = 2
    while counter < n:
        current += 1
        for i in range(2, int(current ** 0.5) + 1):
            if current % i == 0:
                break
        else:
            counter += 1
    return current


# 1-ый алгоритм решета
def sieve_1(n):
    max_n = n * 30
    table = [False for _ in range(max_n)]
    counter = 0
    current = 1

    while counter < n:
        current += 1
        if not table[current]:
            counter += 1
            for i in range(current, max_n, current):
                table[i] = True
    return current


# 2-ой алгоритм решета
def sieve_2(n):
    primes = [2]
    counter = 3
    while len(primes) < n:
        flag = True
        end = int(counter ** 0.5) + 1
        for i in primes:
            if counter % i == 0:
                flag = False
                break
            if i > end:
                break
        if flag:
            primes.append(counter)
        counter += 2
    return primes[-1]


if __name__ == '__main__':
    n = 1
    for i in range(5):
        n *= 5
        prime_res = timeit('prime(n)', globals=globals(), number=100)
        sieve_res1 = timeit('sieve_1(n)', globals=globals(), number=100)
        sieve_res2 = timeit('sieve_2(n)', globals=globals(), number=100)
        print(f"Func=prime N={n} Time={prime_res:.4f}",
              f"Func=sieve_1 N={n} Time={sieve_res1:.4f}",
              f"Func=sieve_2 N={n} Time={sieve_res2:.4f}",
              '*' * 50, sep='\n')


# **************************************************
# Func=prime N=5 Time=0.0012
# Func=sieve_1 N=5 Time=0.0031
# Func=sieve_2 N=5 Time=0.0008
# **************************************************
# Func=prime N=25 Time=0.0158
# Func=sieve_1 N=25 Time=0.0274
# Func=sieve_2 N=25 Time=0.0072
# **************************************************
# Func=prime N=125 Time=0.1197
# Func=sieve_1 N=125 Time=0.1181
# Func=sieve_2 N=125 Time=0.0514
# **************************************************
# Func=prime N=625 Time=0.7456
# Func=sieve_1 N=625 Time=0.6000
# Func=sieve_2 N=625 Time=0.4122
# **************************************************
# Func=prime N=3125 Time=6.7224
# Func=sieve_1 N=3125 Time=3.0778
# Func=sieve_2 N=3125 Time=2.8730
# **************************************************

# Дополнительные запуски. number = 1
# **************************************************
# Func=sieve_1 N=10000 Time=0.1328
# Func=sieve_2 N=10000 Time=0.1256
# **************************************************
# Func=sieve_1 N=80000 Time=0.9608
# Func=sieve_2 N=80000 Time=1.9467
# **************************************************
#
#
# Сложность у всех алгоритмов квадратичная
# Самый медленный prime, однако на малых числах он даже обгоняет sieve_1
# sieve_2 работает быстрее всех где-то до 100_000 (10000-ное простое число), потом его обгоняет sieve_1
# sieve_2 когда-то (года 3.5 назад) сам придумал, когда нужно было написать решето, а реализации на сишке я ещё не знал)
