def palindrom(a):
    n=len(a)
    for i in range(n):
        if (a[i]!=a[n-i-1]): return False
    return True
