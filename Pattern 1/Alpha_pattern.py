n = int(input())

a = 65

for i in range(1,n+1):

    for j in range(1, i+1):
        print("%c" %(a), end="")
    a +=1
    print()