guest_hame=input()
host_name=input()
pile=input()
t=guest_hame+host_name

if sorted(t)==sorted(pile):
    print("YES")
else:
    print("NO")