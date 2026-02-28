def f(n, k):
    if n == k:
        return 1
    if n < k:
        return 0
    return f(n-2, k) + f(n-3, k) + f(n//5, k)
print(f(56, 10)*f(10, 6)*f(6, 1))
