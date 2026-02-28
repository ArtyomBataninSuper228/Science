
def f(n, k):
    if n == k:
        return 1
    if n < k:
        return 0
    if n >= 30 and n <= 45:
        return 0
    return f(n-4, k)+f(n-11, k)+f(n//2, k)
print(f(120, 20))