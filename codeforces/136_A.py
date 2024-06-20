N=int(input())
p=list(map(int,input().split(" ")))
recieved_from=[0 for _ in range(N)]
for i in range(N):
    giver=p[i]
    recieved_from[giver-1]=i+1
print(" ".join(map(str,recieved_from)))




