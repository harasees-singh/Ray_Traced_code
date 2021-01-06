import time 
import math
n=int(input())
start = time.time()
def prime_testimony(n):
    if n == 1:
        return False
    elif n==2 or n==3 :
        return True
    elif n%6 == 1 or n%6 == 5:
        for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
            if n%i == 0:
                return False
        return True
    else:
        return False
    
print(prime_testimony(n))
print(time.time() - start)