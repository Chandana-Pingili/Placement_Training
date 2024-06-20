n=int(input())
ans=[]
for i in range(n):
    s=input()
    if len(s)>10:
        r=s[0]+str(len(s)-2)+s[-1]
        ans.append(r)
    else:
        ans.append(s)
print("\n".join(ans))
