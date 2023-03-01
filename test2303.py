import sys

k, n1 = map(int, sys.stdin.readline().split())
n2 = k - n1

bi = 1

while True:
    if k > n1:
       bi *= k
       k -= 1
    
    else:
        if n2 > 1:
            bi //= n2 
            n2 -= 1
        else:
            break
    
print(bi)