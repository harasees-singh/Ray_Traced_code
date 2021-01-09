import math
import os
import random
import re
import sys

# input format first line: n(size) k(obstacles)
# second line : r c (position of queen)
# subsequent lines positions of obstacles

def queensAttack(n, k, r_q, c_q, obstacles):
    list_of_eliminations=[0, 0, 0, 0, 0, 0, 0, 0] #the ith element will eventually be equal to no. of cells covered by some obstacle in the ith direction. we have 8 directions north, south, east, north east, south east, west, north west and finally south west
    for i in range(k):
        eliminations, count_corresponding_to_eliminations = relative_position(obstacles[i]) #assigning the possible eliminations to the particular direction
        
        if list_of_eliminations[count_corresponding_to_eliminations] < abs(eliminations):
            list_of_eliminations[count_corresponding_to_eliminations] = abs(eliminations) #we wish to subtract only the largest no. of cells from one particular dimension or so to say take into consideration the obstacle closest to queen in a given direction
        
    n_square = n_raw(n, r_q, c_q) #this returns possible moves by the queen in case of zero obstacles

    for l in range(8):
        

        n_square = n_square - list_of_eliminations[l] #simply subtracting all the eliminated cells from n_square

    return n_square

def n_raw(n, r_q, c_q):
    
    
    count = n-1 + n-1 + (n-max(r_q, c_q)) + (min(r_q-1, n-c_q))  + (min(r_q, c_q)-1) + (min(c_q-1, n-r_q)) #no. of possible moves by the queen based on mathematical pattern
    return count
        


        

    
         
def relative_position(obstacle): #returning the no. of cells hindered by an obstacle (an integer) and the concerned direction in terms of a no. from 0 to 7
    count = 0
    if obstacle[1] == c_q:
        if obstacle[0] > r_q:
            return n-obstacle[0]+1, count
            
        else:
            
            return obstacle[0], count+1
            

    elif obstacle[1] > c_q:
        
        if obstacle[1]-c_q==obstacle[0]-r_q:
            return n+1-max(obstacle[0], obstacle[1]), count+2

        elif obstacle[1]-c_q==-(obstacle[0]-r_q):
            return min(obstacle[0], n+1-obstacle[1]), count+3

        elif obstacle[0] == r_q:
            return  n-obstacle[1]+1, count+4
        
        else:
            return (0, 0)
    
    elif obstacle[1] < c_q:
        if obstacle[1]-c_q==obstacle[0]-r_q:
            
            return min(obstacle[0], obstacle[1]), count+5
        elif obstacle[1]-c_q==-(obstacle[0]-r_q):
            
            return min(obstacle[1], n+1-obstacle[0]), count+6
        elif obstacle[0] == r_q:
            
            return  obstacle[1], count+7
        else:
            return (0, 0)
    
    


nk = input().split()

n = int(nk[0])

k = int(nk[1])

r_qC_q = input().split()

r_q = int(r_qC_q[0])

c_q = int(r_qC_q[1])

obstacles = []

for _ in range(k):
    obstacles.append(list(map(int, input().rstrip().split())))
    
result = queensAttack(n, k, r_q, c_q, obstacles)
print(result)

