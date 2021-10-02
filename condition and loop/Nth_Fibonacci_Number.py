n = int(input())
f1 = 1
f2 = 1
f = 1
i = 3
while(i<=n):
    f = f1 + f2
    f1 = f2
    f2 = f
    i = i + 1
print(f)     
    