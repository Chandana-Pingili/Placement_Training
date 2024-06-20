n=int(input())
res=[]
pattern="YES"
for i in range(n):
    s=input().upper()
    if s==pattern:
        res.append("YES")
    else:
        res.append("NO")
print("\n".join(res))