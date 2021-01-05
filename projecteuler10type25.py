# this code prints primes less than the number taken as input starting from 2
import time
import math
x = int(input("enter num here :) "))

t = time.time()


def prime(num):
    if num == 2:
        return True
    if num == 3:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, math.floor(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


collection = [2, 3]

for k in range(1, x//6 + 2):
    if prime(6*k - 1) and (6*k - 1) < x:
        collection.append(6*k - 1)
    if prime(6*k + 1) and (6*k + 1) < x:
        collection.append(6*k + 1)



print(collection)
print(f"execution time = {time.time()- t}")
