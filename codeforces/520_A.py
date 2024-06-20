import string
n=int(input())
s=input().lower()
alpha=string.ascii_lowercase
if n<26:
    print("NO")
else:
    for c in alpha:
        if c not in s:
            print("NO")
            break
    
    else:
        print("YES")