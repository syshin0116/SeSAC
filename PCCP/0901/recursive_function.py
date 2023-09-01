def func(x):
    if x== 1:
        return None
    func(x - 1)
    return x


def fibo(n):
    if n<=2:
        return 1
    return fibo(n-1) + fibo(n)


n=1
lst = [0] * (n+1)
def fibo(n):
    if lst[n]:
        return lst[n]
    else:
        lst[n] = fibo(n-1) + fibo(n-2)
        return lst[n]