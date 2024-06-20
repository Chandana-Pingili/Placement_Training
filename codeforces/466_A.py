n,m,a,b=map(int,input().split(" "))
c1=0
c2=0
c3=n*a

c4=(n//m)*b+(n%m)*a
c1=((n//m)+1)*b
c2=(n//m)*b+(n%m)*b
print(min(c1,c2,c3,c4))