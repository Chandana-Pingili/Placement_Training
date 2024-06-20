'''for given input n count the numbers which have exactly 3 divisors '''
def countfactors(N):
    i=1
    c=0
    while i*i<=N:
        if N%i==0:
            c+=1
            if i!=N//i:
                c+=1
        i+=1
    return c
def exactly3Divisors(N):
    ans=[]
    for i in range(4,N+1):
        c=countfactors(i)
        if c==3:
            ans.append(i)

    return len(ans)
        
a=exactly3Divisors(10)
print(a)