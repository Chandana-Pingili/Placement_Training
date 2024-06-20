s=input()
l=[]
u=[]
for char in s:
    if char.islower():
        l.append(char)
    else:
        u.append(char)
if len(l)>len(u) or len(l)==len(u):
    print(s.lower())
else:
    print(s.upper())