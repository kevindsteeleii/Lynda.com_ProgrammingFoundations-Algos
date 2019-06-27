def gcd(m, n):
    while n != 0:
        t = m
        m = n
        n = t % n
    return m

print(gcd(12, 16))