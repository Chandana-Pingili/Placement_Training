a,b=map(int,input().split(" "))
no_of_years=0
if a==b:
    no_of_years=1
else:
    while b>=a:
        a*=3
        b*=2
        no_of_years+=1
print(no_of_years)
