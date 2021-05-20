A = [0] * 1000
top = 0
print ("up-down program")
x = int(input())
while x!=0:    
    A[top] = x
    top += 1 
    x = int(input())   
else:
    print("up-down now")

for i in range(top, -1, -1):
    print(A[i])
x = int(input())