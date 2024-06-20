n=int(input())
res=[]
for i in range(n):
    c=input()
    if c in "codeforcces":
        res.append("yes")
    else:
        res.append("NO")
print("\n".join(res))