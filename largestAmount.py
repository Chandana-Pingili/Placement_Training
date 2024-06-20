'''
ip: jobs=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
amount=[5,6,5,4,11,2]

op: 17

explanation : by doing jobs (2,5) and (5,8) we can earn maximum amount'''
def largestAmount(jobs,amount):
    n=len(jobs)
    sj=sorted(jobs)
    c=[]
    for i in range(n):
        c.append([0]*n)
    i=0
    while i<n:
        c[i][i]=amount[jobs.index(sj[i])]
        ii=i
        j=i+1
        while j<n:
            if sj[j][0]>=sj[ii][1]:
                id=jobs.index(sj[j])
                c[i][j]=c[i][j-1]+amount[id]
                ii=j
                j+=1
            else:
                c[i][j]=c[i][j-1]
                j+=1
        i+=1
    m=0
    print(c)
    for i in c:
        if i[-1]>m:
            m=i[-1]
    print(m)

def dpLargestAmount(jobs,amount):
    a=list(amount)
    for i in range(1,len(a)):
        for j in range(i):
            if jobs[j][1]<=jobs[i][0]:
                if a[j]+amount[i]>a[i]:
                    a[i]=a[j]+amount[i]
    print(max(a))
    print(a)
jobs=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
amount=[5,6,5,4,11,2]
largestAmount(jobs,amount)
dpLargestAmount(jobs,amount)
