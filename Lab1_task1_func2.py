def func(a):
    max_int=0
    while (a>0):
        b=a%10
        if (b>max_int and b%3!=0): max_int=b
        a=a//10
    return max_int
