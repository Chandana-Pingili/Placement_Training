a,b,c=map(int,input().split(" "))
if b<a and c>0:
    print("NO")
elif a<b and c<0:
    print("NO")
elif c==0:
    if a==b:
        print("YES")
    else:
        print("NO")
elif (b-a)%c==0:
    print("YES")
else:
    print("NO")