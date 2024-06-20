import string
def sort_alpha(order,s):
    ans=''
    for char in order:
        if char in s:
            ans=ans+(char*s.count(char))
    return ans
n= int(input())
for i in range(n):
    order=input()
    s=input()
    ans=sort_alpha(order,s)
    print(ans)
    


