n = int(input())
Sum_of_Even_Digits= 0
Sum_of_Odd_Digits=0
x=0

while(n>0):
    x=n%10
    if (x%2==0):
        Sum_of_Even_Digits= Sum_of_Even_Digits + x
    else:
        Sum_of_Odd_Digits = Sum_of_Odd_Digits + x
    n=n//10    
        
print(Sum_of_Even_Digits , Sum_of_Odd_Digits)
# print(Sum_of_Odd_Digits)

