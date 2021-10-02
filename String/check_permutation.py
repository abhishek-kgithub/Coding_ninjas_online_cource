def permutation(s1,s2):
    if len(s1)!=len(s2):
        return False
    if sorted(s1)==sorted(s2):
        return True
    else:
        return False
             

s1=input()
s2=input()
if permutation(s1,s2)==True:
    print("true")
else:
    print("false")