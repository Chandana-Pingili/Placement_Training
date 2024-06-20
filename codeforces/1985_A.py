def swap(a,b):
    a,b=b[0]+a[1:],a[0]+b[1:]
    return " ".join((a,b))
n=int(input())
for i in range(n):
    a,b=input().split(" ")
    print(swap(a,b))