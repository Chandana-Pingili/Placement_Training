n=int(input())

ranges=[]
for i in range(n):
    rl=list(map(int,input().split()))
    ranges.append(rl)
left,right=map(int,input().split())
res=[False]*(right-left+1)
for start,end in ranges:
    for i in range(max(left,start),min(end,right)+1):
        res[i-left]=True
if all(res):
    print("True")
else:
    print("False")
    
