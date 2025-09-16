def nod(a, b):
    c = min(a, b)
    for i in range(c, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def count_non_coprime_evens(n):
    count = 0 
    for i in range(2, n, 2):  
        if nod(i, n) > 1:
            count += 1
    return count

n = 12
print(count_non_coprime_evens(n)) 