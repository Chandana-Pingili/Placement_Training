import string
str1="chandana"
f=str1.index("a")
l=str1.rindex("a")
print(f)
sub=str1[f+2:l]
print(sub.index("a"))
print(str1.count("an"))


def s(*l):
    print(l)
s(1,2,3,4,5,6,7,8,9)

def printNums(n):
    if n==0:
        return
    print(n)
    return printNums(n-1)
printNums(5)