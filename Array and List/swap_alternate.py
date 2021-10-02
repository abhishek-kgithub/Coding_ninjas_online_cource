from sys import stdin
def swapAlternate(li, n):
    l = len(li)
    if l%2 == 0:
        for i in range(0,l,2):
            li[i],li[i+1] = li[i+1],li[i]
        return li
    else:
        for i in range(0,l-1,2):
            li[i],li[i+1] = li[i+1],li[i]
        return li
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#Printing the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    arr, n = takeInput()
    if n != 0 :
        swapAlternate(arr, n)
        printList(arr, n)
    t -= 1