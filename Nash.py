N = 2 # N strategies for both players

def  index(i, j):
    """ Returns the index of 1D array 
        that corresponds to element (i, j) of 2D matrix. 
    """
    return i * N + j 

def is_nash(i, j):
    """ Checks if the set of strategies (i, j) is Nash equilibrium.
        If it is Nash equilibrium, returns True. Else returns False. 
    """
    for k in range (N):
        if A[index(k, j)] > A[index(i,j)] :
            return False
        if B[index(i,k)] > B[index(i, j)] :
            return False
    return True            
##################################################################

A = [0] * N * N
B = [0] * N * N
for i in range(N * N):
    A[i] = int(input())
    B[i] = int(input())
for i in range(N):
    for j in range(N):
        if is_nash(i, j):
            print (i + 1, ";", j + 1, " is Nash")


         