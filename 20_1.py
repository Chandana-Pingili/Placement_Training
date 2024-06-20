class OOPs:
    def __init__(self):
        self.s=set()
    def insert(self,s):
        self.s.add(s)
    def search(self,s):
        return s in self.s
    def isPrefix(self,s):
        j=len(s)
        c=0
        for word in self.s:
            if s==word[:j]:
                c+=1
        return c
    def delete(self,s):
        self.s.remove(s)
n=int(input())
while n:
    k=int(input())
    obj=OOPs()
    for i in range(k):
        m,s=input().split()
        if m=="1":
            obj.insert(s)
        elif m=="2":
            print(obj.search(s))
        elif m=="3":
            print(obj.isPrefix(s))
        else:
            obj.delete(s)
    n-=1