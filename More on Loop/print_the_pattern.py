n = int(input())
k = 0
n1 = n - n//2
for i in range(1, n1 + 1):
    for j in range(1, n+1):
        print(k * n+ j, end = '')
        print(" ",end="")
    print()
    k = k + 2
n2 = n - n1
if n % 2 == 0:
    k = n - 1
else:
    k = n - 2
for i in range(1, n2 + 1):
    for j in range(1, n + 1):
        print(k * n + j, end = '')
        print(" ",end="")
        
    print()
    k = k - 2




#  1    2   3    4   5
#  11   12  13   14  15
#  21   22  23   24  25
#  16   17  18   19  20
#  6    7    8   9   10
