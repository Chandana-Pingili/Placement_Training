#print elements which has occured odd number of times

l=input().split()
res=[]
for ele in l:
    if l.count(ele)%2!=0 and ele not in res:
        res.append(ele)
print(res)
#count of characters in string

name=input()

res={}
for char in name:
    if char not in res:
        res[char]=1
    else:
        res[char]+=1
print(res)

#sorting list with nested lists according to second element in the list

l=int(input())
test_cases=[]
for i in range(l):
    t=list(map(int,input().split()))
    t[1]=int(t[1])
    test_cases.append(t)
for i in range(len(test_cases)):
    for j in range(len(test_cases)-1):
        if test_cases[j][1]>test_cases[j+1][1]:
            test_cases[j],test_cases[j+1]=test_cases[j+1],test_cases[j]
print(test_cases)

#find sum of frst 3 minimum elements in the list

l1= list(map(int,input().split()))
res=[]
for ele in l1:
    if ele not in res:
        res.append(ele)
res.sort()
print(sum(res[:3]))

# segregate list as even and odd then merge the list as even in descending order
# and odd in ascending order

l1= list(map(int,input().split()))
el=[x for x in l1 if x%2==0]
ol=[x for x in l1 if x%2!=0]
el.sort(reverse=True)
ol.sort()
print(el+ol)


#print product of the elements in the list which are within the given range1
l1= list(map(int,input().split()))
l,r=map(int,input().split())
res_list=[x for x in l1 if x>=l and x<=r]
product=1
for i in res_list:
    product*=i
print(product)








