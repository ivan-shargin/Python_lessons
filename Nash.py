N = 2 # N strategies for both players

def  index(i, j):
    return i * N + j 

def is_nash(i, j):
    for k in range (N):
        if A[index(k, j)] > A[index(i,j)] :
            return False
        if B[index(i,k)] > B[index(i, j)] :
            return False
    return True            
############################################################################################

A = [0] * N * N
B = [0] * N * N
for i in range(N * N):
    A[i] = int(input())
    B[i] = int(input())
for i in range(N):
    for j in range(N):
        if is_nash(i, j):
            print (i + 1, ";", j + 1, " is Nash")


         