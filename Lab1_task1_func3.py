def coprime(a,b):
    minimum=min(a,b)
    for d in range(2,minimum):
        if (a%d==0 and b%d==0):
            return False
    return True

def func(n):
    min_d=1
    for d in range(2,n):
        if (n%d==0): 
            min_d=d
            break
    max_d=0
    for i in range(2,n):
        if (coprime(i,n)==False and (i%min_d!=0 or min_d==1)):
            max_d=i
    
    sum=0
    while (n>0):
        a=n%10
        if (a<5): sum+=a
        n=n//10
    
    return sum*max_d

print(func(12))