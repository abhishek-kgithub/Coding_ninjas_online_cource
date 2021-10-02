n = int(input())
i = 1
# p = i
while i <= n:
    j = 1
    while j <= i:
        print(i-j+1, end="")
        # p = p+1
        j = j + 1
    print()
    i = i + 1