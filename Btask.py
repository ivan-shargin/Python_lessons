import math

y1 = int(input())
x1 = int(input())
y2 = int(input())
x2 = int(input())

if x1 == x2 :
    print("YES")
elif y1 == y2 :
    print("YES")
elif math.fabs(x2 - x1) == math.fabs(y2 - y1) :
    print("YES")
else : 
    print("NO")
